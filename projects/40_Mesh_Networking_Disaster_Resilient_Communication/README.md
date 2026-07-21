# Mesh Networking Platform for Disaster-Resilient Communication

---

## Executive Summary

This project proposes the design and implementation of a **Mesh Networking Platform for Disaster-Resilient Communication** — a decentralized, self-healing ad-hoc network infrastructure designed to maintain critical text, voice, and location communications when primary infrastructure (cellular towers, internet backbones, power grids) fails due to natural disasters or cyberattacks. The platform runs on low-cost hardware nodes (ESP32/Raspberry Pi with LoRa/Wi-Fi) using a custom mesh routing protocol, backed by a link-quality prediction module that anticipates link failures and proactively re-routes traffic before packet loss occurs.

**Motivation:** During major disasters (earthquakes, floods, hurricanes), cellular networks collapse within minutes due to power loss or physical damage to cell towers. Emergency responders, medical teams, and civilians are left isolated. A peer-to-peer mesh network requires zero centralized infrastructure: every node acts as both a terminal and a relay router. Building this system requires deep knowledge of wireless networking protocols, mobile ad-hoc routing (BATMAN / OLSR), low-level socket programming, mesh topology algorithms, and predictive routing models.

**Objectives:**
- Design a hybrid physical mesh node (ESP32 + LoRa for long-range low-bandwidth text/GPS; Raspberry Pi + Wi-Fi mesh for local voice/data).
- Implement a self-healing Mobile Ad-Hoc Network (MANET) routing protocol handling node joins, departures, and mobility dynamically.
- Build a Store-and-Forward delay-tolerant networking (DTN) module to queue messages when destination paths are temporarily broken.
- Implement a Link-Quality Prediction Subsystem that monitors Signal-to-Noise Ratio (SNR) and Received Signal Strength Indicator (RSSI) trends to predict link dropouts and trigger proactive route updates.
- Develop an Offline First Field Operations App (Progressive Web App / Android) featuring peer-to-peer messaging, offline vector maps, and emergency SOS broadcasting.

**Expected Impact:** A lifesaving cyber-physical communication infrastructure that guarantees field connectivity during total blackout conditions, demonstrating mastery of computer networking, embedded systems, and predictive algorithms.

**Target Users:** Disaster response agencies (Red Cross / Red Crescent, Civil Defense), emergency medical services, search-and-rescue teams, and outdoor/remote expedition teams.

---

## Problem Statement

1. **Infrastructure Single Point of Failure:** Cellular networks rely on centralized towers and fiber backhaul. When towers lose power or backhaul is severed, the network is completely dead.
2. **Dynamic & Unstable Topologies:** Nodes in a disaster zone are mobile (first responders moving). Links constantly form, degrade, and break. Standard IP routing (BGP/OSPF) cannot adapt to rapid MANET changes.
3. **Bandwidth Asymmetry:** LoRa provides 10km+ range but < 10 kbps bandwidth (text/GPS only). Wi-Fi mesh provides 54 Mbps but < 200m range. Routing must intelligently select medium based on payload priority.
4. **Packet Drop Storms:** Traditional reactive routing protocols only search for a new route *after* a link breaks, causing high packet loss during critical emergency transmissions.

---

## Existing Solutions

### Commercial Solutions
- **goTenna Pro:** Commercial tactical mesh radio. Proprietary, expensive ($1,000+ per unit), military/govt pricing.
- **Sonim / Beartooth:** Specialized hardware mesh devices.

### Open-Source Solutions
- **Meshtastic:** Open-source LoRa mesh network project for off-grid messaging. Great community project, but relies on flood routing with limited bandwidth management and no proactive predictive routing.
- **Disaster Radio:** Open-source solar-powered LoRa mesh network (inactive development).
- **B.A.T.M.A.N. (Better Approach To Mobile Adhoc Networking):** Linux kernel layer-2 mesh routing protocol. Excellent for Wi-Fi, but not optimized for hybrid LoRa/Wi-Fi topologies.

### Limitations of Existing Solutions
- Meshtastic uses simple multi-hop flooding, which causes packet collisions as node density scales.
- B.A.T.M.A.N. is Wi-Fi layer-2 only and does not handle ultra-low-bandwidth radio links (LoRa) or predictive link degradation.
- No existing open-source project combines multi-radio hybrid routing (LoRa + Wi-Fi) with ML-based proactive link failure prediction.

---

## Proposed Solution

Build **AeroMesh**, a disaster-resilient communications platform:

1. **Hardware Node Architecture:**
   - **Long-Range Node (Edge):** ESP32 + SX1276 LoRa transceiver (868/915 MHz) for long-range (up to 10km) low-bandwidth telemetry, GPS coordinates, and short text SOS messages.
   - **High-Capacity Gateway Node:** Raspberry Pi 4 + Wi-Fi Mesh + LoRa concentrator module acting as local high-speed mesh relay and local web server.
2. **Hybrid Mesh Routing Engine:** A C++/Go daemon executing a modified distance-vector routing algorithm that considers link bandwidth, latency, packet loss rate, and energy availability to select optimal multi-hop paths.
3. **Delay-Tolerant Networking (DTN) Engine:** Store-and-Forward queue. If a recipient is unreachable, intermediate nodes store the encrypted payload in local flash memory until a path becomes available (epidemic / bundle routing).
4. **Link-Quality Prediction Module:** A lightweight time-series model (Exponential Smoothing / Linear Regression / Random Forest) running on gateway nodes that analyzes RSSI/SNR sliding windows. If a link's quality is dropping rapidly, it alerts the routing engine to switch traffic to a backup path *before* the active link severs.
5. **Field Responder App:** A offline-capable Progressive Web App (PWA) hosted directly on the gateway nodes. First responders connect their standard smartphones to the local gateway Wi-Fi and immediately access chat, map coordinates (Leaflet offline tiles), and SOS dispatch screens without installing an app store app.

---

## System Architecture

### Embedded & Hardware Layer
- **ESP32 Firmware:** C++ (using PlatformIO / Arduino framework) for low-power LoRa packet framing, MAC layer CSMA/CA, and sleep cycles.
- **Raspberry Pi Daemon:** C++ / Go for high-speed Wi-Fi mesh (batman-adv or custom user-space routing daemon).

### Backend / Edge Server (on Gateway Node)
- **Local API Server:** Go (lightweight, zero-dependency REST/WebSocket server).
- **Routing & DTN Engine:** C++ / Go service managing route tables, bundle queues, and link metric tables.

### Frontend
- **Field App:** React (PWA with Service Workers for offline asset caching).
- **Offline Maps:** Leaflet.js rendering pre-loaded OpenStreetMap vector tiles stored on the Raspberry Pi node.

### Security
- **End-to-End Encryption (E2EE):** Curve25519 + AES-GCM-256 encryption for private peer-to-peer messages.
- **Node Authentication:** Public key cryptography; malicious/rogue nodes cannot inject false routing tables or tamper with messages.

### AI Components

| Component | Role | Technique | AI % |
|-----------|------|-----------|------|
| Link Quality Failure Prediction | Predict link dropouts from RSSI/SNR degradation trends to trigger proactive re-routing | Sliding-window trend analysis + Random Forest / Linear Regression | ~15% |

**Total AI effort: ~15%.** If the link prediction module is disabled, the routing engine falls back to reactive link failure detection (re-routing only after missed ACKs). The mesh network remains 100% operational.

### Databases
- **SQLite (on-node):** Storage of local message bundles, user identity keys, and offline map metadata.
- **In-Memory Route Table:** Active mesh topology state stored in RAM for sub-millisecond lookup.

### Networking
- **LoRa MAC (868/915 MHz):** Custom TDMA/CSMA frame structure.
- **Wi-Fi 802.11s / 802.11g ad-hoc:** Layer-2 mesh networking.
- **Protobuf:** Compact binary serialization over low-bandwidth links.

### DevOps
- **PlatformIO:** Embedded firmware build toolchain for ESP32.
- **Docker:** Gateway node software packaging.
- **Network Simulator (ns-3):** Simulate 50+ node mesh mobility scenarios during testing.

---

## Research Opportunities

1. **Proactive vs. Reactive Routing in MANETs:** Benchmark packet delivery ratio (PDR) and latency of predictive RSSI-based re-routing vs. traditional reactive routing (AODV/DSR) in high-mobility scenarios.
2. **Hybrid LoRa/Wi-Fi Routing Metrics:** Research multi-objective routing metrics balancing link bandwidth (Mbps vs. kbps), hop count, and node battery life.
3. **Store-and-Forward Buffer Management:** Evaluate buffer eviction strategies (TTL vs. priority vs. FIFO) when intermediate node memory becomes full during prolonged isolation.

---

## Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **Hardware** | ESP32 + SX1276 LoRa, Raspberry Pi 4 | Physical mesh nodes |
| **Languages** | C++ (PlatformIO) | Embedded ESP32 firmware & routing engine |
| | Go | Gateway local server & DTN engine |
| | TypeScript | PWA frontend application |
| **Protocols** | LoRa PHY, 802.11s Wi-Fi Mesh, Protobuf | Wireless physical layer & data serialization |
| **AI / ML** | Scikit-learn / Custom C++ Regression | Link quality degradation predictor |
| **Databases** | SQLite | On-device message store & node directory |
| **Frontend** | React, PWA, Leaflet.js | Offline map & field messaging UI |
| **Simulation** | ns-3 Network Simulator | Large-scale MANET topology testing |

---

## Required Knowledge

| Topic | Importance | Where to Learn |
|-------|-----------|----------------|
| Wireless Sensor Networks & MANET Routing | Essential | Computer Networking textbooks (Kurose & Ross) / MANET literature |
| Embedded C++ & LoRa Communication | Essential | ESP32 & RadioLib documentation |
| Delay-Tolerant Networking (DTN) Concepts | Essential | RFC 4838 (Delay-Tolerant Networking Architecture) |
| Offline Web Applications (PWAs & WebSockets) | Important | MDN Web Docs (PWA Service Workers) |
| Basic Cryptography (AES-GCM, ECC) | Important | Applied Cryptography resources |

---

## Suggested Team Distribution

| Member | Role | Responsibilities | Key Technologies |
|--------|------|-----------------|------------------|
| **Member 1** | Embedded LoRa Engineer | Develop ESP32 firmware, CSMA/CA MAC layer, LoRa packet transmission, and power management. | C++, PlatformIO, LoRa / SX1276 |
| **Member 2** | Mesh Routing Protocol Eng. | Implement hybrid routing daemon, link metric table, and neighbor discovery protocol. | C++ / Go, Networking Sockets |
| **Member 3** | DTN & Security Engineer | Build Store-and-Forward bundle queue, ECC key exchange, and AES-GCM end-to-end encryption. | Go, Cryptography, SQLite |
| **Member 4** | AI & Link Prediction Eng. | Develop link-quality prediction model (RSSI/SNR time-series), integrate with routing daemon, run ns-3 simulations. | Python / C++, ns-3, Scikit-learn |
| **Member 5** | PWA & Offline Maps UI Dev | Build offline React PWA, integrate Leaflet offline vector maps, build chat and SOS broadcast interface. | React, PWA, Leaflet.js, WebSockets |

---

## Estimated Budget

| Item | Cost (EGP) | Cost (USD) |
|------|-----------|-----------|
| 4× ESP32 + SX1276 LoRa Transceiver Modules | 3,200 | ~65 |
| 2× Raspberry Pi 4 (Gateway nodes) | 9,000 | ~180 |
| Antennas, batteries, 3D printed enclosures | 2,000 | ~40 |
| **Total** | **~14,200 EGP** | **~285 USD** |

---

## Difficulty
**Score: 9/10**
Designing custom wireless protocols at the byte level, dealing with RF noise, implementing custom ad-hoc routing, and ensuring sub-second PWA connection over local Wi-Fi without internet is a comprehensive cyber-physical challenge.

---

## Innovation
**Score: 9/10**
Combines low-power long-range LoRa hardware, high-bandwidth local Wi-Fi mesh, predictive link degradation re-routing, and zero-install offline PWA mapping into a single emergency response system.

---

## Career Value
**Wireless / Network Systems Engineer:** ⭐⭐⭐⭐⭐
**Embedded Software Engineer:** ⭐⭐⭐⭐⭐
**Cyber-Physical Systems / Defense Tech Developer:** ⭐⭐⭐⭐
