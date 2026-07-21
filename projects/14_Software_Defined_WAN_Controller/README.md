# Software-Defined WAN (SD-WAN) Controller

---

## Executive Summary

This project proposes the design and implementation of a **Software-Defined Wide Area Network (SD-WAN) Controller**. The system abstracts network hardware, allowing administrators to manage routing policies, monitor link health, and dynamically steer traffic across multiple WAN links (e.g., MPLS, Broadband, 4G/LTE) from a centralized software dashboard, rather than configuring individual hardware routers via CLI.

**Motivation:** Traditional networking relies on decentralized, hardware-specific configuration. Software-Defined Networking (SDN) separates the "control plane" (where routing decisions are made) from the "data plane" (where packets are forwarded). Building an SD-WAN controller teaches students the fundamentals of modern network engineering, OpenFlow protocols, and dynamic traffic engineering—skills critical for modern telecom and cloud infrastructure.

**Objectives:**
- Build a centralized Controller capable of communicating with edge network devices via SDN protocols (OpenFlow or NETCONF/YANG).
- Implement dynamic path selection algorithms that route traffic based on real-time link quality (latency, jitter, packet loss).
- Develop a software-based edge router (using Linux networking primitives, eBPF, or Open vSwitch) to act as the Customer Premises Equipment (CPE).
- Create a web dashboard for network topology visualization, policy configuration, and traffic monitoring.

**Expected Impact:** A functional SD-WAN prototype that demonstrates how software can intelligently route traffic over unreliable internet links to provide enterprise-grade reliability.

**Target Users:** Network Engineers, ISPs, and Enterprise IT departments managing branch office connectivity.

---

## Problem Statement

Managing corporate networks across multiple branch offices is a nightmare:
1. **Inflexibility:** Configuring routing protocols (BGP, OSPF) on individual hardware routers is slow, manual, and error-prone.
2. **Cost:** MPLS (dedicated private lines) is highly reliable but extremely expensive. Broadband internet is cheap but unreliable.
3. **Application Awareness:** Traditional routers route based on IP addresses. Modern businesses need to route based on application (e.g., "Send Zoom traffic over the best link, send background backups over the cheapest link").
4. **Visibility:** Detecting a degraded link (high jitter, dropping packets) before it completely fails is difficult without centralized telemetry.

---

## Existing Solutions

### Commercial Solutions
- **Cisco Viptela:** Market-leading enterprise SD-WAN.
- **VMware SD-WAN (VeloCloud):** High-performance, cloud-delivered SD-WAN.
- **Fortinet Secure SD-WAN:** Integrates SD-WAN with Next-Gen Firewalls.

### Open-Source Solutions
- **OpenDaylight / ONOS:** Open-source SDN controllers. (Heavy, complex, primarily used by large telecoms).
- **flexiWAN:** Open-source SD-WAN platform.

### Limitations of Existing Solutions
- Commercial solutions are closed boxes.
- Open-source SDN controllers like OpenDaylight are massive Java monoliths that take months just to understand, masking the underlying network physics from students.

---

## Proposed Solution

Build **AeroRoute**, a lightweight SD-WAN architecture consisting of:

1. **Edge Router (vCPE):** A software router built on Linux. It establishes secure VPN tunnels (WireGuard or IPsec) to other branches, continuously probes link health (ICMP/UDP echo), and applies QoS policies.
2. **Central Controller:** The "brain." It maintains the global network topology, receives telemetry from all Edge Routers, calculates optimal routing paths, and pushes forwarding rules down to the edges.
3. **Analytics Engine:** Processes telemetry data to visualize link degradation and automatically trigger path failovers.
4. **Admin Dashboard:** A React UI where admins can define high-level policies (e.g., "VoIP gets highest priority and requires < 50ms latency") rather than writing routing tables.

---

## System Architecture

### Backend (Control Plane)
- **Controller:** Python or Go. (Go is preferred for high-concurrency network I/O).
- **Communication Protocol:** gRPC or WebSockets for Controller <-> Edge Router communication. OpenFlow if interacting with physical SDN switches.

### Backend (Data Plane / Edge)
- **Routing/Forwarding:** Linux `tc` (Traffic Control), `iproute2`, and iptables/nftables orchestrated by a local Go daemon. Alternatively, use Open vSwitch (OVS) controlled via OpenFlow.
- **VPN:** WireGuard (highly performant, modern crypto).

### Frontend
- **Dashboard:** React with a network topology visualization library (e.g., vis.js or React Flow).

### AI Components
- **Predictive Link Degradation (Optional):** Using time-series machine learning (e.g., ARIMA or LSTMs) to predict when a broadband link is likely to fail or degrade based on historical telemetry, allowing preemptive traffic steering.

### Databases
- **PostgreSQL:** Network topology, policies, and configuration state.
- **InfluxDB / Prometheus:** Storing high-frequency link telemetry (latency, jitter, packet loss).

### Networking
- **Underlay:** The physical internet connections (Simulated using Mininet or multiple cloud VMs).
- **Overlay:** The encrypted VPN tunnels connecting the branches.

---

## Required Knowledge

| Topic | Importance | Where to Learn |
|-------|-----------|----------------|
| Linux Networking (`iproute2`, `tc`) | Essential | Linux man pages |
| VPN Protocols (WireGuard/IPsec) | Essential | WireGuard whitepaper |
| SDN Concepts & OpenFlow | Important | SDN Textbooks / ONF resources |
| Go Systems Programming | Important | Go documentation |
| Time-Series Data & Telemetry | Important | Prometheus docs |

---

## Suggested Team Distribution

| Member | Role | Responsibilities | Key Technologies |
|--------|------|-----------------|-----------------|
| **Member 1** | Edge Data Plane Eng. | Build the software router (vCPE), configure WireGuard tunnels, and implement packet steering/QoS using Linux networking APIs or Open vSwitch. | C/Go, Linux Networking, OVS |
| **Member 2** | Network Controller Eng. | Build the centralized Controller that calculates routes, maintains the topology graph, and pushes policies to the edges. | Go, Graph Algorithms, gRPC |
| **Member 3** | Telemetry & Analytics Eng. | Implement continuous link probing (latency/jitter/loss), store telemetry, and build the logic for dynamic path failover. | Go/Python, InfluxDB, Prometheus |
| **Member 4** | Platform Backend Eng. | Build the REST API for the dashboard, handle user authentication, and manage configuration state in the database. | Python/Node.js, PostgreSQL |
| **Member 5** | Frontend & Visualization | Build the React dashboard, specifically focusing on the dynamic, interactive network topology map and charting link quality. | React, vis.js, Recharts |

---

## Estimated Budget

| Category | Item | Cost (EGP) | Cost (USD) |
|----------|------|-----------|-----------|
| **Cloud** | 5-6 VMs across different geographic regions to simulate wide-area latency and actual branch offices. | 10,000 | ~200 |
| **Total** | | **~10,000 EGP** | **~200 USD** |

---

## Difficulty
**Score: 9/10**
Deep knowledge of the Linux network stack, kernel routing, and distributed state management is required. Debugging network loops and routing black holes across a distributed system is extremely challenging.

---

## Innovation
**Score: 8/10**
While SD-WAN is the industry standard, building a custom controller and software router provides a profound educational experience that few university programs offer.

---

## Career Value
**Network Engineer (SDN):** ⭐⭐⭐⭐⭐ (Telecoms are desperate for software-literate network engineers)
**Systems / C / Go Programmer:** ⭐⭐⭐⭐
**Cloud Infrastructure Engineer:** ⭐⭐⭐⭐
