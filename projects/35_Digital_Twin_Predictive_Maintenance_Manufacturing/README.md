# Digital Twin Platform for Predictive Maintenance in Manufacturing

---

## Executive Summary

This project proposes the design and implementation of a **Digital Twin Platform for Predictive Maintenance in a Manufacturing Environment**. The system creates persistent, synchronized software replicas (digital twins) of physical manufacturing equipment — CNC machines, industrial motors, conveyor systems — by continuously ingesting high-frequency sensor telemetry (vibration, temperature, current draw, acoustic emissions). A failure-prediction ML module analyzes the twin's state history to forecast equipment failure 24–72 hours in advance, enabling maintenance teams to intervene before costly unplanned downtime occurs.

**Motivation:** Unplanned equipment downtime costs manufacturers an estimated $50 billion annually worldwide. Predictive maintenance — using sensor data to predict failures before they occur — is the engineering answer. But implementing it requires solving several hard problems: ingesting high-frequency sensor data from industrial hardware, maintaining real-time synchronized digital twin state, building accurate failure prediction models on imbalanced data (failures are rare), and delivering actionable insights to maintenance teams. This project addresses all four.

**Objectives:**
- Design an edge-to-cloud data ingestion pipeline for high-frequency (1 kHz+) sensor telemetry from multiple machines.
- Build a digital twin state engine that maintains a real-time model of each machine's operational state and health trajectory.
- Implement a failure prediction ML model (survival analysis or LSTM) trained on historical sensor data with failure labels.
- Build a maintenance work order system that automatically generates, prioritizes, and assigns maintenance tickets.
- Create a 3D visualization dashboard showing the factory floor with real-time twin health indicators.

**Expected Impact:** A production-grade predictive maintenance platform demonstrating mastery of industrial IoT data engineering, digital twin architecture, and applied ML for time-series — one of the most valuable skill sets in modern manufacturing.

**Target Users:** Manufacturing companies (automotive, pharmaceutical, food processing), facility management companies, industrial equipment OEMs, and maintenance service providers.

---

## Problem Statement

1. **Reactive Maintenance is Expensive:** Waiting for equipment to fail (run-to-failure) causes unplanned downtime, emergency repair costs, and production loss. 
2. **Scheduled Maintenance is Wasteful:** Replacing parts on a fixed schedule (every 3 months) wastes parts that still have useful life and misses failures that develop faster than the schedule.
3. **Data Fragmentation:** Sensor data from different machines uses different formats, protocols, and time resolutions. Building a unified view across a factory requires heavy ETL work.
4. **Class Imbalance in Failure Data:** Failures are extremely rare (< 0.1% of all sensor readings). Standard ML models trained on imbalanced data simply predict "no failure" always and achieve 99.9% accuracy while being useless.

---

## Existing Solutions

### Commercial Solutions
- **Predix (GE):** Industrial IoT and digital twin platform. Enterprise pricing.
- **SAP Predictive Maintenance:** SAP enterprise integration. Very expensive.
- **Uptake / Aspentech:** Industrial AI platforms. Closed source.
- **Azure Digital Twins / AWS IoT TwinMaker:** Cloud-native digital twin services.

### Limitations
- All commercial platforms are expensive, vendor-locked, and opaque.
- Building on Azure Digital Twins is configuration work, not engineering — the platform hides all the interesting problems.
- No open-source platform combines edge ingestion, twin state management, survival analysis, and an operational maintenance workflow system.

---

## Proposed Solution

Build **AeroTwin Manufacturing**, a complete predictive maintenance digital twin platform:

1. **Edge Sensor Nodes:** Raspberry Pi or industrial mini-PCs co-located with each machine, collecting vibration (MPU-6050 accelerometer), temperature (DS18B20), current (ACS712 Hall effect sensor), and acoustic emissions. High-frequency data (1 kHz vibration) processed locally (FFT feature extraction) before cloud upload.
2. **Edge-to-Cloud Pipeline:** MQTT/AMQP messages sent to a cloud broker. Apache Kafka buffers the stream; an Apache Flink job performs real-time feature engineering (RMS, kurtosis, crest factor from raw vibration).
3. **Digital Twin State Engine:** A Go service maintaining a persistent in-memory + database representation of each machine's current state: health score, operating mode, maintenance history, and current feature vector.
4. **Failure Prediction Module:** A survival analysis model (Cox Proportional Hazards or Weibull distribution) or LSTM trained on the NASA CMAPSS turbofan dataset (public benchmark) to predict Remaining Useful Life (RUL). Handles class imbalance using SMOTE + cost-sensitive learning.
5. **Maintenance Work Order System:** When predicted RUL falls below a configurable threshold (e.g., < 48 hours), automatically generates a maintenance work order with severity, recommended action, and assigned technician.
6. **3D Factory Dashboard:** A Three.js-powered 3D factory floor visualization where each machine is represented as a colored 3D model (green = healthy, yellow = degrading, red = critical). Real-time health updates pushed via WebSocket.

---

## System Architecture

### Edge Layer
- **Hardware:** Raspberry Pi 4 + sensors (MPU-6050, DS18B20, ACS712).
- **Software:** Python — sensor reading, local FFT computation, MQTT publishing.

### Cloud Backend
- **Ingestion:** Eclipse Mosquitto (MQTT broker) → Apache Kafka.
- **Stream Processing:** Apache Flink (feature engineering: RMS, kurtosis, frequency band energy).
- **Twin Engine:** Go — manages twin state, health scoring, and ML inference requests.
- **ML Microservice:** Python (FastAPI) — hosts the trained RUL prediction model.

### Frontend
- **Dashboard:** React with Three.js for 3D factory floor visualization.
- **Operations UI:** Work order management, maintenance history, alert inbox.

### AI Components

| Component | Role | Technique | AI % |
|-----------|------|-----------|------|
| Remaining Useful Life (RUL) Prediction | Predict hours until equipment failure using degradation signals | Cox Proportional Hazards (survival analysis) or LSTM on time-series features | ~25% |
| Health Score Computation | Compute a 0–100 health indicator from real-time features | Weighted combination of z-score deviations from baseline | ~5% |

**Total AI effort: ~25–30%.** Remove it → the digital twin still provides real-time monitoring, feature visualization, and historical trending. Maintenance teams switch from predictive to threshold-based alerting.

### Databases
- **PostgreSQL:** Machine inventory, maintenance history, work orders, technician assignments.
- **InfluxDB:** High-frequency time-series sensor features (post-FFT).
- **Redis:** Live twin state cache for fast dashboard rendering.

### Networking
- **MQTT:** Edge-to-cloud sensor telemetry.
- **Apache Kafka:** Cloud-level event bus.
- **WebSocket:** Real-time twin health updates to the 3D dashboard.
- **REST:** Work order management API, ML inference endpoint.

### DevOps
- **Docker + Kubernetes:** All cloud services containerized.
- **Ansible:** Edge node provisioning automation.
- **GitHub Actions:** CI/CD.

---

## Research Opportunities

1. **Survival Analysis vs. LSTM for RUL Prediction:** Benchmark Cox PH vs. LSTM-based RUL prediction on the NASA CMAPSS dataset — comparing prediction accuracy, confidence intervals, and data efficiency.
2. **Edge FFT Compression Efficiency:** Quantify the bandwidth reduction achieved by transmitting FFT features (10 values) vs. raw vibration waveforms (1,000 samples/second).
3. **Digital Twin Synchronization Latency:** Measure the end-to-end latency from a physical sensor event to the digital twin state update.
4. **Maintenance Schedule Optimization:** Research the financial impact of switching from fixed-schedule maintenance to model-driven predictive maintenance on a simulated factory.

---

## Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Hardware** | Raspberry Pi 4, MPU-6050, ACS712 | Edge sensor nodes |
| **Languages** | Python | Edge data collection, ML service, Flink jobs |
| | Go | Digital twin engine, REST APIs |
| | TypeScript | 3D dashboard frontend |
| **Messaging** | MQTT (Mosquitto), Apache Kafka | Edge-to-cloud ingestion |
| **Processing** | Apache Flink | Real-time feature engineering |
| **AI** | Lifelines (Cox PH) / PyTorch (LSTM) | RUL prediction model |
| **Databases** | PostgreSQL | Operational data |
| | InfluxDB | Sensor feature time-series |
| | Redis | Twin state cache |
| **Frontend** | React, Three.js | 3D factory floor dashboard |
| **DevOps** | Docker, Kubernetes, GitHub Actions | CI/CD and deployment |

---

## Suggested Team Distribution

| Member | Role | Responsibilities | Technologies |
|--------|------|-----------------|--------------|
| **Member 1** | Edge IoT & Sensing | Set up Raspberry Pi sensor nodes, implement vibration FFT, publish MQTT telemetry. | Python, C, MQTT, Raspberry Pi |
| **Member 2** | Data Pipeline Engineer | Configure Kafka ingestion, build Flink stream processing jobs for feature extraction. | Python, Kafka, Flink |
| **Member 3** | AI / Predictive Maintenance | Train RUL prediction model on NASA CMAPSS; handle class imbalance; deploy as REST microservice. | Python, Lifelines, PyTorch |
| **Member 4** | Digital Twin Engine & Backend | Build the Go twin state engine, work order system, maintenance scheduling API. | Go, PostgreSQL, Redis |
| **Member 5** | 3D Dashboard Engineer | Build the Three.js 3D factory floor; implement real-time health status overlays via WebSocket. | React, Three.js, WebSocket |

---

## Estimated Budget

| Item | Cost (EGP) | Cost (USD) |
|------|-----------|-----------|
| 2× Raspberry Pi 4 + sensors | 8,000 | ~160 |
| Cloud infrastructure (Kafka, K8s) | 10,000 | ~200 |
| **Total** | **~18,000 EGP** | **~360 USD** |

---

## Difficulty
**Score: 8/10** — High-frequency vibration data processing requires DSP knowledge (FFT). The 3D Three.js dashboard is a significant frontend challenge. Survival analysis for RUL prediction is more statistically sophisticated than standard classification.

## Innovation
**Score: 8/10** — Combining real IoT hardware, a persistent twin engine, survival analysis ML, and a 3D interactive dashboard is a genuinely novel and visually impressive engineering system.

## Sponsor Potential
**Score: 9/10** — Any manufacturing company — automotive plants, cement factories, pharmaceutical production — is an immediate potential sponsor.

## Career Value
**IoT / Industrial Data Engineer:** ⭐⭐⭐⭐⭐
**ML Engineer (Industrial AI):** ⭐⭐⭐⭐⭐
**Frontend / 3D Visualization Engineer:** ⭐⭐⭐⭐

---

## References

1. Saxena, A., et al. (2008). "Damage Propagation Modeling for Aircraft Engine Run-to-Failure Simulation." *PHM Conference.* (NASA CMAPSS Dataset)
2. ISO 13374: Condition Monitoring and Diagnostics of Machines.
3. Heng, A., et al. (2009). "Rotating Machinery Prognostics: State of the Art, Challenges and Opportunities." *Mechanical Systems and Signal Processing.*
4. Three.js Documentation: https://threejs.org/docs/
5. Lifelines (Survival Analysis in Python): https://lifelines.readthedocs.io/
