import psutil
import os

# Iterate over all running process
for proc in psutil.process_iter(['pid', 'name']):
    try:
        # Get process details as a dictionary
        pinfo = proc.info
        print(f"Process ID: {pinfo['pid']}")
        print(f"Process Name: {pinfo['name']}\n")
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

# Run the notepad process for example
os.system("notepad.exe")
