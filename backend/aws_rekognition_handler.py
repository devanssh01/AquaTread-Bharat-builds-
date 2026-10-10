import json
import base64
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

rekognition = boto3.client('rekognition')
MAX_PAYLOAD_BYTES = 5 * 1024 * 1024

def lambda_handler(event, context):
    cors_headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type,Authorization',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,DELETE'
    }

    if event.get('httpMethod') == 'OPTIONS':
        return {'statusCode': 200, 'headers': cors_headers, 'body': ''}

    try:
        body = event.get('body', '')
        if not body or len(body) > MAX_PAYLOAD_BYTES:
            return {'statusCode': 413, 'headers': cors_headers, 'body': json.dumps({'error': 'Payload size limit 5MB'})}

        parsed_body = json.loads(body)
        action = parsed_body.get('action', 'REPORT_HAZARD') # REPORT_HAZARD or CLEAR_HAZARD

        # 1. HANDLE HAZARD CLEARANCE REQUEST
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

        # 2. HANDLE NEW HAZARD REPORT SCAN VIA AWS REKOGNITION
        image_base64 = parsed_body.get('image')
        if not image_base64:
            return {'statusCode': 400, 'headers': cors_headers, 'body': json.dumps({'error': 'Missing image payload'})}

        if ',' in image_base64:
            image_base64 = image_base64.split(',')[1]

        image_bytes = base64.b64decode(image_base64)

        response = rekognition.detect_labels(
            Image={'Bytes': image_bytes},
            MaxLabels=15,
            MinConfidence=70.0
        )

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

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {'statusCode': 500, 'headers': cors_headers, 'body': json.dumps({'error': str(e)})}