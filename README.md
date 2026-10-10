# AquaTread-Bharat-builds-
Here is the updated `README.md` with **JSSUN Noida, Uttar Pradesh** added for all team members and subtitle references.

You can copy and paste this directly into your `README.md` file in VS Code:

```markdown
# 🌊 AquaTread-Bharat-builds-

> **Vehicle-Adaptive Navigation for Waterlogged Urban Streets**
> Built by **Team ThunderStrike** (JSSUN Noida, Uttar Pradesh) for the **AWS Bharat Build Tour Hackathon** at Delhi Technological University (DTU).

[![Live App](https://img.shields.io/badge/Live%20App-GitHub%20Pages-00D2FF?style=for-the-badge&logo=github)](https://devanssh01.github.io/AquaTread/)
[![AWS Backend](https://img.shields.io/badge/AWS-Rekognition%20%7C%20Lambda-FF9900?style=for-the-badge&logo=amazon-aws)](https://github.com/devanssh01/AquaTread/tree/main/backend)

---

## 📌 The Problem

During heavy monsoon rains in NCR, traditional navigation apps show everyone the exact same route based purely on traffic speeds. But a flooded underpass or waterlogged street that an SUV can cross easily might completely drown a scooter engine or stall a low-clearance sedan.

When commuters trust generic navigation during severe rain, two main issues arise:
1. Vehicles stall inside submerged underpasses, causing massive urban gridlocks.
2. Crowdsourced reporting apps get spammed with fake reports, screenshots, and non-flood photos.

---

## 💡 Our Solution

**AquaTread-Bharat-builds** is a Progressive Web App (PWA) designed to calculate safe detour routes based on your **vehicle's physical ground clearance**. 

Instead of blocking roads globally for everyone, AquaTread-Bharat-builds checks reported waterlogging depths against your active vehicle profile. If a waterlogged area is too deep for your vehicle and intersects your calculated path, the app automatically reroutes you around the danger zone using OSRM detour waypoint logic.

---

## ✨ Core Features

### 🛵 1. Vehicle Clearance Tolerances
AquaTread-Bharat-builds evaluates road safety against three distinct vehicle tiers:
* 🛵 **Two-Wheelers:** Reroutes if water depth exceeds **15 cm** (Ankle deep).
* 🚗 **Sedans:** Safe in ankle deep; reroutes if depth exceeds **30 cm** (Knee deep).
* 🚙 **SUVs / 4x4s:** Clears ankle and knee deep; reroutes if depth exceeds **45 cm** (Engine deep).

### 🤖 2. 3-Step Anti-Fake Security Pipeline
Crowdsourced hazard reporting usually breaks down due to fake submissions. AquaTread screens every uploaded photo using a 3-step check:
1. **AWS Rekognition & Canvas Spectrum Analysis:** Scans image pixels for genuine water reflections and monsoon surface ripples. Rejects:
   * **Screenshots & UI Graphics:** Catches OS screenshot filenames and map UI artifacts.
   * **Human Hands & Body Photos:** Uses RGB warm hue spectrum checking ($R > G > B$) to reject selfies and hand photos.
   * **Gutter & Sewage Sludge:** Uses algae green/chemical scum spectrum ($G > R + 12$) and black drain hole detection ($RGB < 22$) to block open drains and manholes.
   * **AI / Stock Downloads:** Screens filenames for stock imagery and AI generation signatures.
2. **EXIF GPS Hardware Match:** Confirms the photo metadata matches where the user is currently standing.
3. **Open-Meteo Satellite Rain Radar:** Verifies live rain telemetry ($>2.0\text{ mm/h}$) before logging or clearing hazards from the map.

### 📍 3. High-Contrast Navigation & Live Traffic
* **AquaTread Blue Polyline:** Active route lines are rendered in high-contrast blue (`#00b4d8`) with an ambient outer glow so the path never blends into green traffic roads or dark map tiles.
* **Keyless Google Traffic Layer:** Live Google Traffic tile streams are isolated in a custom Leaflet pane (`trafficTilePane`) to prevent CSS dark-mode inversion filters from corrupting traffic line colors.
* **Vivid Congestion Segments:** Congestion vectors (Red `#dc2626`, Amber `#d97706`, Emerald `#059669`) render along the path for instant long-distance visibility.

### 🏬 4. Local & Private Place Intelligence
* **Nominatim POI Search:** Autocomplete supports local shops (🏬), private office parks (🏢), housing societies (🏡), restaurants, and micro-landmarks using OSM `addressdetails`, `extratags`, and `namedetails`.
* **Draggable Pins & Reverse Geocoding:** Both start and destination markers can be dragged anywhere on the map, updating exact venue names and triggering live OSRM route recalculation on `dragend`.

### ☀️ 5. Monsoon & Summer Heatwave Dual Mode
* **🌧️ Monsoon Mode:** Standard flood detour navigation and waterlogging depth monitoring.
* **☀️ Heatwave Mode:** Switches route styling to highlight municipal drinking water tanker points and emergency hydration hubs during extreme summer heatwaves.

### ⚡ 6. God Mode Sandbox for Testing
* Built-in judge testing toolbar with pre-validated sample tests (`🌊 Valid Flood` vs `☀️ Fake Dry Road`).
* **`💥 Drop Hazard`** drops mid-route flood barriers on demand.
* **`🗑️ Clear Hazards`** wipes sandbox hazards cleanly.

---

## 🏗️ How It Works

```text
[ Commuter PWA ] ──> Select Vehicle (Two-Wheeler / Sedan / SUV)
       │
       ├──> [ Search FROM & TO ] ──> OSRM Engine calculates route
       │                                  │
       └──> [ Hazard Reported ] ──────────┼──> Checks water depth vs vehicle clearance
                                          │
                                          └──> Clear Blue Route or Safe Detour
```

---

## 🛠️ Tech Stack

* **Frontend:** HTML5, Vanilla JavaScript (ES6+), CSS3, Progressive Web App (PWA).
* **Mapping Engine:** Leaflet.js (v1.9.4), OpenStreetMap base tiles, Google Transparent Live Traffic tile stream.
* **Routing & Geocoding:** OSRM (Open Source Routing Machine) API, Nominatim Search & Reverse Geocoding API.
* **Weather Telemetry:** Open-Meteo Weather Satellite API.
* **Backend Verification:** AWS Rekognition, AWS Lambda, Python `boto3` SDK (`backend/aws_rekognition_handler.py`).

---

## 👥 Team ThunderStrike

* **Hiya Khanna** — JSSUN Noida, Uttar Pradesh
* **Ayati** — JSSUN Noida, Uttar Pradesh
* **Srishti** — JSSUN Noida, Uttar Pradesh
* **Devansh Upadhyay** — JSSUN Noida, Uttar Pradesh

---

## 🔗 Links

* **Live PWA App:** https://devanssh01.github.io/AquaTread-Bharat-builds-/
* **Backend Source Code:** [AquaTread-Bharat-builds GitHub Repository (Backend)]https://github.com/devanssh01/AquaTread-Bharat-builds-/blob/a245d3d520a09ef9a7fc068d805e9179cdca8e91/backend/aws_rekognition_handler.py
* **Technical Blog:** Published on AWS Builder Center *(Link updated upon publishing)*
* **Event:** Bharat Build Tour (DTU Delhi) by AWS & WeMakeDevs
```

       
