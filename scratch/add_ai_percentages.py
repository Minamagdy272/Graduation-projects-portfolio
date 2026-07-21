import os

PROJECTS_DIR = r"c:\GP\projects"

ai_percentages = {
    "02_Realtime_Fraud_Detection_Pipeline": "~20%",
    "03_Zero_Trust_Network_Access_Platform": "~15%",
    "04_Realtime_Collaborative_Code_Editor": "~10%",
    "05_Industrial_IoT_Predictive_Maintenance": "~20%",
    "06_End_to_End_MLOps_Platform": "~20%",
    "08_Privacy_Preserving_Healthcare_Data_Exchange": "~25%",
    "09_Edge_Native_Video_Analytics_Pipeline": "~30%",
    "10_Digital_Twin_Smart_Building_Management": "~15%",
    "11_Peer_to_Peer_Energy_Trading_Platform": "~15%",
    "12_Realtime_Data_Lakehouse_Platform": "~10%",
    "13_Intelligent_API_Gateway": "~15%",
    "14_Software_Defined_WAN_Controller": "~15%",
    "15_Smart_City_Traffic_Optimization": "~30%",
    "17_Automated_Penetration_Testing_Framework": "~15%",
    "19_Self_Healing_Infrastructure_Platform": "~15%",
    "20_Remote_Patient_Monitoring_Platform": "~15%",
    "23_Distributed_Log_Analytics_Anomaly_Detection": "~25%",
    "24_Smart_Agriculture_Monitoring_System": "~25%",
    "25_Multi_Cloud_Cost_Intelligence_Platform": "~20%",
    "26_Multi_Tenant_GPU_Scheduling_Platform": "~15%",
    "27_Multi_Region_Active_Active_DB_Replication": "~15%",
    "28_IDS_Industrial_Control_Networks_SCADA": "~20%",
    "29_Multi_Robot_Coordination_Warehouse_Fleets": "~15%",
    "30_Time_Series_DB_Engine_Industrial_Telemetry": "~15%",
    "31_Insider_Threat_Behavioral_Monitoring": "~25%",
    "32_5G_Network_Slicing_Management_Platform": "~15%",
    "33_In_Vehicle_Network_Gateway_CAN_Bus": "~20%",
    "34_Automotive_Digital_Twin_ECU_Testing": "~15%",
    "35_Digital_Twin_Predictive_Maintenance_Manufacturing": "~25%",
    "36_Cross_Border_Micropayment_Settlement": "~15%",
    "37_Core_Banking_Microservices_Platform": "~15%",
    "38_Microgrid_Control_System_Islanded_Operation": "~15%",
    "39_SIEM_Correlation_Engine": "~15%",
    "40_Mesh_Networking_Disaster_Resilient_Communication": "~15%"
}

def update_readme(folder, percentage):
    path = os.path.join(PROJECTS_DIR, folder, "README.md")
    if not os.path.exists(path):
        print(f"Skipping {folder}: file not found.")
        return
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    pct_header = f"\n**Total AI Subsystem Effort:** {percentage} of overall engineering work (bounded building block)\n"
    
    # Check if already present
    if "Total AI Subsystem Effort:" in content:
        # replace existing
        import re
        content = re.sub(r"\*\*Total AI Subsystem Effort:\*\*.*?\n", pct_header.strip() + "\n", content)
    else:
        # insert right after "## AI Components"
        target = "## AI Components\n"
        if target in content:
            content = content.replace(target, target + "\n" + pct_header.strip() + "\n")
        else:
            # fallback append
            content += "\n" + pct_header

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated {folder}: added AI percentage {percentage}")

for folder, pct in ai_percentages.items():
    update_readme(folder, pct)

print("All 34 projects updated with explicit AI percentage callouts.")
