from shutil import copy2, rmtree
import requests
import urllib
import ctypes
import ast
import sys
import os

# Program directory
AppPath = os.path.dirname(__file__)  

def ShowMessage(msg, title="Update failed", msg_type=0x00000010):
    return ctypes.windll.user32.MessageBoxW(0, msg, title, msg_type)

def InstallUpdate():
    """Download and install the latest version of the program"""

    # Configurable parameters
    config_url="https://github.com/Ariel-MN/UpdateCheck/releases/latest/download/update.json"
    config_output=os.path.join(AppPath,'..','etc','update.json')
    temp_output=os.path.join(AppPath,'..','etc','~tmp')

    try:
        # Create tmp folder
        os.makedirs(temp_output, exist_ok=True)
        os.system(f"attrib +h {temp_output}")

        # Download config file
        urllib.request.urlretrieve(config_url,config_output)

        # Read config file
        with open(config_output, "r") as f:
            data=f.read()
            files=ast.literal_eval(data)["files"]

        # Download update program files
        for f in files:
            urllib.request.urlretrieve(f["url"],os.path.join(temp_output,f["filename"]))

        # Move program files to the correct directory
        for f in files:
            copy2(os.path.join(temp_output,f["filename"]),os.path.join(AppPath,'..',f["output"]))

        # Remove tmp folder
        rmtree(temp_output)
    except Exception as e:
        ShowMessage(f"While installing the new update, the following error occurred: {e}")

def NewUpdate(current_version):
    """Check if there is a new version available on Github"""

    # Configurable parameters
    latest_release = "https://api.github.com/repos/Ariel-MN/UpdateCheck/releases/latest"

    try:
        # Get latest version
        last_version = requests.get(latest_release).json()["tag_name"]

        if current_version != last_version:
            return ShowMessage(msg="Would you like to upgrade now?", title=f"New update available {last_version}", msg_type=0x00000044)==6
        else:
            ShowMessage(msg=f"Program version {last_version} is up to date!", title="No Updates Available", msg_type=0x00000040)
            return False
    except Exception as e:
        ShowMessage(f"While checking for new a update, the following error occurred: {e}")


if __name__ == "__main__" and len(sys.argv)>1:
    
    program_curr_version = sys.argv[1]
    program_path = sys.argv[2]
    
    if NewUpdate(program_curr_version):
        InstallUpdate()

    try:
        # Flush buffer
        sys.stdout.flush()
    finally:
        # Kill process and start main program
        os.execl(sys.executable, os.path.join(AppPath,'..','lib','pythonw.exe'), program_path)
