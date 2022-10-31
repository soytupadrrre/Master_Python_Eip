$cred = Get-Credential -UserName 'DOMAIN\USERNAME' -Message ' '

Start-Process Powershell.exe -Credential $cred -ArgumentList '-noprofile -command &{Start-Process Powershell -verb runas}'