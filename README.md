# 💧 AquaTread — Vehicle-Adaptive Emergency Navigation PWA

> **AWS Bharat Build Tour Hackathon Submission** | **Team ThunderStrike**  
> *Devansh Upadhyay, Hiya Khanna, Ayati, Srishti (JSSUN Noida)*

Live PWA Demo: [https://devanssh01.github.io/AquaTread-Bharat-builds-/](https://devanssh01.github.io/AquaTread-Bharat-builds-/)

---

## 🎯 The Problem
During monsoons, traditional navigation apps (Google Maps, Waze) treat all vehicles identically. A 15cm flooded underpass causes binary road closures for everyone—forcing unnecessary detours for heavy SUVs while guiding scooters straight into deep water traps.

## ⚡ How AquaTread Solves It
AquaTread introduces a **Vehicle Clearance Matrix** paired with a **4-Layer Anti-Fake AI Verification Engine**:
* 🛵 **Two-Wheeler (15cm threshold):** Reroutes around ankle-deep waterlogging.
* 🚗 **Sedan (30cm threshold):** Passes ankle water, reroutes around knee-deep floods.
* 🚙 **SUV / 4x4 (45cm threshold):** Safely passes mild/moderate water, saving time & fuel.

---

## 🏆 Competitive Landscape: Why AquaTread Wins

| Feature | 🚗 Google Maps / Waze | 📍 MapMyIndia (Mappls) | 🏛️ Govt Portals | 💧 AquaTread (Our App) |
|---|---|---|---|---|
| **Routing Logic** | Binary (Open/Closed) | Static Waterlog Pins | Macro-level Text Alerts | **Vehicle-Adaptive Clearance Thresholds** |
| **Fake Report Protection** | ❌ None (Spam Prone) | ❌ None | ❌ Manual (Slow) | **✅ 4-Layer AI Engine (Canvas + AWS Rekognition)** |
| **Rain Verification** | ❌ No Weather Crosscheck | ❌ No Weather Crosscheck | ❌ No API Crosscheck | **✅ Open-Meteo Weather Radar Live API** |
| **Monsoon Performance** | Heavy App (100MB+) | Heavy Web App | Clunky Govt Portal | **✅ Sub-300ms Offline-Cached Single-File PWA** |
| **Emergency Heatwave** | ❌ None | ❌ None | ❌ Static List | **✅ Overpass API 3km Water Point Mapping** |

---

## 🛡️ 4-Layer Anti-Fake Shield
1. **HTML5 Canvas Pixel Spectrum Scan:** Rejects screenshots, indoor lighting, skin tones, and sewage/gutters on client-side.
2. **AWS Rekognition AI (Cloud):** Lambda backend verifies asphalt/street context via Boto3, rejecting glassware/indoors.
3. **Open-Meteo Rain Radar API:** Cross-checks active precipitation (>2.0mm/h) at report coordinates.
4. **Proximity & EXIF Geofence:** Locks submissions within 50m radius of live user GPS.

---

## 🛠️ Tech Stack & AWS Services
* **AWS Services:** AWS Lambda, Amazon Rekognition (Boto3 Python SDK), AWS S3
* **Map & Routing:** Leaflet JS 1.9.4, Custom Layer Panes, OSRM Driving API (16 Waypoint Offsets)
* **APIs:** Nominatim OpenStreetMap, Open-Meteo Weather API, Overpass OSM Drinking Water API
---

## 📁 Project Structure
---

AquaTread-Bharat-builds-/
├── index.html # Complete Single-File PWA (Frontend + Logic)
└── backend/
└── aws_rekognition_handler.py # AWS Lambda + Amazon Rekognition (Boto3)

## 🚀 How to Run Locally
1. Clone the repo
2. Open `index.html` in any modern browser (Chrome/Edge recommended)
3. Allow Location permission when prompted
4. For AWS Rekognition: Deploy `aws_rekognition_handler.py` as Lambda function

## 🎥 Demo Video
*(Paste your YouTube/Drive demo video link here once recorded)*