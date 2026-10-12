# 💧 AquaTread — Vehicle-Adaptive Emergency Navigation PWA

> **AWS Bharat Build Tour Hackathon Submission** | **Team ThunderStrike**  
> *Devansh Upadhyay, Hiya Khanna, Ayati, Srishti (JSSUN Noida)*

Live PWA Demo: [https://devanssh01.github.io/AquaTread-Bharat-builds-/](https://devanssh01.github.io/AquaTread-Bharat-builds-/)

Blog link: <Author: Devansh Upadhyay> https://builder.aws.com/content/3KQhSQkeRYCMIEM7x3TQ1DkQIO6/aquatread-bharat-how-we-built-vehicle-aware-navigation-with-aws-ai

## 🧪 30-Second Quick Testing Guide for Judges

If you are testing the live app, follow these 4 quick steps:

| Step | Action | What Happens (Tech Under the Hood) |
| :--- | :--- | :--- |
| **1. Dynamic Rerouting** | Click **`⚡ God Mode`** ➔ Double-click anywhere on the blue route line | Drops a simulated flood hazard. App dynamically triggers OSRM rerouting to bypass the hazard instantly! |
| **2. Vehicle Matrix Check** | Toggle between **`🛵 Bike (15cm)`**, **`🚗 Sedan (30cm)`**, **`🚙 SUV (45cm)`** | Rerouting logic filters water depths based on vehicle exhaust height clearance. |
| **3. Anti-Fake Shield** | Click **`📸 Report Flood`** & upload an image | Runs **Canvas RGB pixel scanner** (rejects skin/clothes/dry roads), queries **Open-Meteo Rain Radar (mm/h)**, and triggers **AWS Rekognition AI**. |
| **4. Heatwave Safe-Haven** | Click **`🔥 Heatwave`** toggle | Queries live **Overpass API** for real OpenStreetMap drinking water points within 3km radius. |
| **5. Recenter Map** | Click **`🎯` Bullseye** | Instantly flies camera back to live GPS user coordinates. |

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

## 🚀 Quick Start & Testing Options

### Option 1: Instant Live Web App (No Setup Required)
Directly open the live PWA in your browser:
👉 **[https://devanssh01.github.io/AquaTread-Bharat-builds-/](https://devanssh01.github.io/AquaTread-Bharat-builds-/)**

---

### Option 2: Run Locally on Your Computer
1. **Clone the repository:**
   ```bash
   git clone https://github.com/devanssh01/AquaTread-Bharat-builds-.git
   Open the Application:
2. Double-click index.html to open it in Chrome, Edge, or Firefox.
   No npm install, node_modules, or local server setup required!
3. Grant Location Permission: Allow GPS access when prompted to initialize live routing.
4. Test Rerouting Engine: Click ⚡ God Mode on the top bar and double-click anywhere on the map route to drop simulated flood hazards.


## 🎥 Demo Video
https://www.youtube.com/shorts/qjZKb658yzY?si=YeeABpSWcImCUGCj