#https://www.cyberdrain.com/monitoring-with-powershell-monitoring-storage-spaces-and-windows-raid/

try {
    $RAIDState = Get-VirtualDisk | where-object { $_.OperationalStatus -ne "OK"}
    }
    catch {
        write-output "Command has Failed: $($_.Exception.Message)"
        exit 1
    }
     
    if ($RAIDState) {
        write-output "Check Diagnostics. Possible RAID failure."
        write-output $RAIDState
        exit 1
    }
    else {
        write-output "Healthy - No StorageSpace issues found"
    }
