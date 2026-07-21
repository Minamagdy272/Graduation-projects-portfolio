import os
import re

PROJECTS_DIR = r"c:\GP\projects"

def get_project_folders():
    folders = [f for f in os.listdir(PROJECTS_DIR) if os.path.isdir(os.path.join(PROJECTS_DIR, f))]
    return sorted(folders)

print(f"Found {len(get_project_folders())} project folders.")
