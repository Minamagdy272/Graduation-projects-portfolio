# Microgrid Control System for Islanded Operation

---

## Executive Summary

This project proposes the design and implementation of a **Microgrid Control System for Islanded Operation** — a decentralized power management and control platform designed to manage localized electricity grids (combining solar PV, battery storage, diesel generators, and critical/non-critical loads). The system automatically handles grid-tied versus islanded mode transitions during main grid failures, balances power supply and demand in real-time, and uses a generation/demand forecasting module to optimize energy storage dispatch and generator runtime.

**Motivation:** Climate change, aging national power grids, and frequent blackouts make microgrids essential for hospitals, military bases, industrial parks, and remote communities. Operating a microgrid when disconnected from the main utility grid ("islanded mode") is an extreme cyber-physical engineering challenge: voltage and frequency must be maintained dynamically without the stabilizing anchor of the national grid. Building this control system requires expertise in embedded control loops, industrial protocols (Modbus, IEC 61850), real-time optimization, and time-series forecasting.

**Objectives:**
- Build a hardware-in-the-loop (HiL) or simulated electrical microgrid environment modeling generation (Solar PV, Battery Energy Storage System - BESS, Diesel Generator) and loads.
- Implement an automated Islanding Detection and Transition Engine that decouples the microgrid safely upon utility grid fault detection within < 50ms.
- Develop a Secondary Frequency and Voltage Control loop to stabilize the islanded grid under sudden load changes.
- Implement a generation and load demand forecasting module using time-series models to predict next-day solar generation and load profiles.
- Build an Economic Dispatch and Optimization Service that schedules battery charging/discharging and generator start/stop sequences to minimize fuel costs and maximize renewable self-consumption.
- Create a SCADA/HMI web dashboard for microgrid operators.

**Expected Impact:** A robust, resilient cyber-physical energy control platform demonstrating mastery of industrial IoT, real-time control systems, time-series forecasting, and power systems engineering.

**Target Users:** Renewable energy developers, industrial facility managers, rural electrification initiatives, military base operators, and utility companies.

---

## Problem Statement

1. **Unstable Islanded Frequency & Voltage:** Without the main grid acting as an infinite bus, sudden changes in solar generation (clouds) or load (heavy motors starting) cause dangerous frequency/voltage spikes or drops that damage equipment.
2. **Seamless Transition Requirement:** Transitioning from grid-connected to islanded mode during a power outage must occur in under 50 milliseconds to prevent blackouts for sensitive critical loads (hospitals, data centers).
3. **Intermittent Renewables:** Solar energy is stochastic. Coordinating battery storage and backup diesel generators without wasting fuel or over-discharging batteries requires predictive foresight.
4. **Multi-Protocol Industrial Interfacing:** Microgrid components use diverse communication standards (Modbus RTU/TCP, DNP3, IEC 61850, MQTT).

---

## Existing Solutions

### Commercial Solutions
- **Schneider Electric EcoStruxure Microgrid Advisor:** Commercial microgrid controller. Proprietary, expensive, closed platform.
- **Siemens Spectrum Power Microgrid Management:** Enterprise utility software.
- **ABB Ability Microgrid Controller:** Hardware-bound proprietary controller.

### Open-Source Solutions
- **OpenDSS (EPRI):** Electric power distribution system simulator (simulation tool, not an operational real-time controller).
- **GridLAB-D:** Distribution system simulation tool developed by US DOE.

### Limitations of Existing Solutions
- Existing tools are either offline simulation models (OpenDSS) or multi-million-dollar proprietary commercial systems (Siemens/Schneider).
- No open-source project provides a complete operational microgrid controller with real-time control loops, forecast-driven economic dispatch, and a modern web-based HMI.

---

## Proposed Solution

Build **AeroGrid Control**, a complete Microgrid Management & Control Platform:

1. **Microgrid Simulation/HiL Layer:** A Python/C++ simulator modeling the physical dynamics of a 500kW microgrid (Solar PV, BESS, Diesel Gen, 3 Load Banks) communicating over Modbus TCP.
2. **Fast Acting Controller (Primary/Secondary Control):** Embedded Go/C++ controller implementing droop control emulation and secondary PI control loops for voltage and frequency stabilization.
3. **Islanding Switch Controller:** Monitors utility grid voltage/frequency vector shift and commands the point of common coupling (PCC) circuit breaker to open upon fault detection.
4. **Energy Management System (EMS) & Economic Dispatch:** A Python optimization service executing linear programming (PuLP/SciPy) every 15 minutes to calculate optimal battery state-of-charge (SoC) targets and generator dispatch schedules.
5. **Generation & Load Forecasting Module:** A Prophet / LSTM time-series model predicting hourly solar irradiance and customer load profile 24 hours ahead based on weather API data and historical telemetry.
6. **Operator SCADA/HMI Dashboard:** A React + D3.js web application rendering an interactive Single-Line Diagram (SLD) of the microgrid with live power flow animations, SoC meters, and manual override controls.

---

## System Architecture

### Backend
- **Real-Time Control Plane:** Go / C++ (low-latency Modbus TCP polling and fast control loops).
- **Optimization & Forecasting Plane:** Python (FastAPI, SciPy, Prophet) for 15-minute dispatch schedules.
- **Communication Protocol:** Modbus TCP for device communication; MQTT for telemetry streaming to dashboard.

### Frontend
- **SCADA Dashboard:** React with TypeScript.
- **Single-Line Diagram:** Interactive SVG/D3.js visualization showing real-time active (kW) and reactive (kVAR) power flow vectors.

### Security
- **TLS 1.3 & mTLS:** Encrypted Modbus TCP over TLS / Secure MQTT.
- **Role-Based Access Control:** Operator vs. Administrator roles (prevent unauthorized breaker trips).
- **Audit Logging:** Immutably logs all switching commands and setpoint changes.

### AI Components

| Component | Role | Technique | AI % |
|-----------|------|-----------|------|
| Solar Generation & Load Forecasting | Predict 24-hour solar output and facility load profile based on weather inputs and history | Prophet / LSTM time-series model | ~15% |

**Total AI effort: ~15%.** If the forecasting module is removed, the Economic Dispatch defaults to rule-based threshold control (e.g., charge battery when solar > load, start generator when battery < 20%). The grid remains fully operational and stable.

### Databases
- **InfluxDB:** High-frequency time-series storage for electrical parameters (V, I, f, P, Q) sampled at 100ms intervals.
- **PostgreSQL:** Configuration data, asset registry, economic dispatch schedules, operator log audit trail.
- **Redis:** Real-time state cache for the fast control loop and SCADA dashboard.

### Networking
- **Modbus TCP:** Industrial device communication (Inverters, Meters, Protection Relays).
- **MQTT / WebSockets:** High-speed SCADA telemetry streaming.

### DevOps
- **Docker Compose:** Package simulation environment, control engine, database, and SCADA dashboard.
- **GitHub Actions:** Automated testing pipeline validating control loop logic against simulated grid disturbances.

---

## Research Opportunities

1. **Seamless Islanding Transition Latency:** Measure and optimize the detection and breaker opening time during simulated grid faults.
2. **Forecast Uncertainty Impact on Microgrid Economics:** Quantify how solar forecast errors affect generator fuel consumption and battery degradation.
3. **Multi-Agent Decoupled Microgrid Control:** Evaluate decentralized vs. centralized control architectures under communication link failures.

---

## Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Languages** | Go / C++ | Real-time control loop, Modbus TCP client |
| | Python | EMS optimization, Forecasting model, API |
| | TypeScript | SCADA Dashboard |
| **Industrial Protocols**| Modbus TCP, MQTT | Device communication and telemetry |
| **AI / ML** | Prophet, Scikit-learn, SciPy | Time-series forecasting & Linear Programming |
| **Databases** | InfluxDB | 100ms electrical telemetry storage |
| | PostgreSQL | System configuration & event logs |
| | Redis | High-speed state cache |
| **Frontend** | React, D3.js, SVG | Interactive Single-Line Diagram dashboard |
| **DevOps** | Docker, GitHub Actions | Containerization and CI/CD testing |

---

## Required Knowledge

| Topic | Importance | Where to Learn |
|-------|-----------|----------------|
| Microgrid Control & Islanding Dynamics | Essential | IEEE Std 2030.7 & 2030.8 (Microgrid Controller Standards) |
| Industrial Communication Protocols (Modbus) | Essential | Modbus Organization specifications & tutorials |
| Real-time Control Loops (PI/PID, Droop Control) | Essential | Control Systems Engineering fundamentals |
| Time-Series Forecasting | Important | Prophet / Scikit-learn documentation |
| React & SVG / D3 Visualization | Important | Web development tutorials for custom SVG manipulation |

---

## Suggested Team Distribution

| Member | Role | Responsibilities | Key Technologies |
|--------|------|-----------------|------------------|
| **Member 1** | Power Systems & Control Lead | Design the microgrid physical simulator, implement droop control and voltage/frequency PI loops. | C++/Python, Control Theory |
| **Member 2** | Industrial Protocol & Edge Eng. | Build Modbus TCP client/server stack, implement islanding detection and breaker control logic. | Go, Modbus TCP, Socket Programming |
| **Member 3** | EMS & Optimization Eng. | Build the Economic Dispatch engine (Linear Programming) and battery state-of-charge optimizer. | Python, SciPy, PuLP |
| **Member 4** | Forecasting & Analytics Eng. | Implement solar generation and load forecasting model; build InfluxDB telemetry pipeline. | Python, Prophet, InfluxDB |
| **Member 5** | SCADA / HMI Frontend Developer | Develop the React web dashboard with an interactive animated Single-Line Diagram. | React, D3.js, WebSockets, SVG |

---

## Estimated Budget

| Item | Cost (EGP) | Cost (USD) |
|------|-----------|-----------|
| Hardware Modbus RTU/TCP Gateway (for testing optional physical hardware) | 4,000 | ~80 |
| Raspberry Pi 4 (dedicated embedded controller host) | 4,500 | ~90 |
| Cloud VPS for telemetry & demo hosting | 2,500 | ~50 |
| **Total** | **~11,000 EGP** | **~220 USD** |

---

## Difficulty
**Score: 9/10**
Combines electrical power systems domain knowledge, tight real-time control constraints (<50ms switching), industrial protocol handling, linear optimization, and complex SVG SCADA graphics.

---

## Innovation
**Score: 9/10**
Provides an open-source, standards-aligned (IEEE 2030.7) microgrid controller incorporating ML-driven dispatch optimization — a sector dominated by multi-million-dollar proprietary systems.

---

## Career Value
**Energy Storage & Microgrid Systems Engineer:** ⭐⭐⭐⭐⭐
**Embedded / Industrial Automation Engineer:** ⭐⭐⭐⭐⭐
**Cyber-Physical Systems / IoT Architect:** ⭐⭐⭐⭐
