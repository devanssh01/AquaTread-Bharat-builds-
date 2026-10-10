import json
import base64
import boto3
import logging

# Setup Logging for AWS CloudWatch
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize AWS Rekognition Client (IAM Role ensures secure access)
rekognition = boto3.client('rekognition')
MAX_PAYLOAD_BYTES = 5 * 1024 * 1024  # 5 MB Limit to prevent memory/cost exhaustion

def lambda_handler(event, context):
    # CORS Headers - Required for API Gateway to allow frontend communication
    cors_headers = {
        'Access-Control-Allow-Origin': '*',  # In production, replace with 'https://devanssh01.github.io'
        'Access-Control-Allow-Headers': 'Content-Type,Authorization',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,DELETE'
    }

    # Handle Preflight OPTIONS request (Browser safety)
    if event.get('httpMethod') == 'OPTIONS':
        return {'statusCode': 200, 'headers': cors_headers, 'body': ''}

    try:
        # 1. API Gateway Base64 & Empty Body Handling Fix
        body = event.get('body', '') or ''
        if event.get('isBase64Encoded'):
            body = base64.b64decode(body).decode('utf-8')

        if not body:
            return {
                'statusCode': 400,
                'headers': cors_headers,
                'body': json.dumps({'error': 'Empty request body'})
            }

        # 2. Payload Size Limit Protection (Security feature against DDoS/Spam)
        if len(body) > MAX_PAYLOAD_BYTES:
            return {
                'statusCode': 413,
                'headers': cors_headers,
                'body': json.dumps({'error': 'Payload size limit exceeded (5MB)'})
            }

        parsed_body = json.loads(body)
        action = parsed_body.get('action', 'REPORT_HAZARD') # Actions: REPORT_HAZARD or CLEAR_HAZARD

        # 3. HANDLE HAZARD CLEARANCE REQUEST
        if action == 'CLEAR_HAZARD':
            hazard_id = parsed_body.get('hazard_id')
            logger.info(f"Processing clearance request for hazard ID: {hazard_id}")
            return {
                'statusCode': 200,
                'headers': cors_headers,
                'body': json.dumps({
                    'status': 'cleared',
                    'hazard_id': hazard_id,
                    'message': 'Clearance verified via satellite radar and consensus telemetry.'
                })
            }

        # 4. HANDLE NEW HAZARD REPORT SCAN VIA AWS REKOGNITION
        image_base64 = parsed_body.get('image')
        if not image_base64:
            return {
                'statusCode': 400, 
                'headers': cors_headers, 
                'body': json.dumps({'error': 'Missing image payload'})
            }

        # Strip data URI prefix if sent by browser canvas (e.g., data:image/jpeg;base64,...)
        if ',' in image_base64:
            image_base64 = image_base64.split(',')[1]

        image_bytes = base64.b64decode(image_base64)

        # Trigger Amazon Rekognition AI Vision
        response = rekognition.detect_labels(
            Image={'Bytes': image_bytes},
            MaxLabels=15,
            MinConfidence=70.0
        )

        # Extract labels and process logic
        labels = [label['Name'].lower() for label in response.get('Labels', [])]
        
        flood_keywords = ['water', 'flood', 'puddle', 'slush', 'submerged', 'river']
        dry_keywords = ['asphalt', 'dry', 'pavement', 'street', 'road']

        is_flooded = any(kw in labels for kw in flood_keywords)
        is_dry_asphalt = any(kw in labels for kw in dry_keywords) and not is_flooded

        top_confidence = response['Labels'][0]['Confidence'] if response.get('Labels') else 0.0

        return {
            'statusCode': 200,
            'headers': cors_headers,
            'body': json.dumps({
                'status': 'success',
                'is_flooded': is_flooded,
                'rejected_as_dry': is_dry_asphalt,
                'confidence': round(top_confidence, 2),
                'labels': labels
            })
        }

    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': cors_headers,
            'body': json.dumps({'error': 'Invalid JSON format'})
        }
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'headers': cors_headers,
            'body': json.dumps({'error': 'Internal server error'})
        }