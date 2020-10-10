# Created 9 Oct 2020 ptf

$rpis = get-content .\rpis.txt
$targetdir = "H:\rpi\"
$sshkey = "C:\Users\patfindley\.ssh\id_rsa.pem"
$date = "get-date -format FileDate"

#Backup Rasberry Pis
foreach ($rpi in $rpis) {
    $img = "$targetdir$rpi$date.img.gz"
    if (test-networkconnection $rpi -port 22)
    {
        ssh -i $sshkey pat@$rpi "sudo dd if=/dev/mmcblk0 bs=10M" | wsl gzip -c> $img
    }
}
# And the rpi4 with an ssd is special
$rpi4img = "H:\rpi\rpi4-19a$date.img.gz"
ssh -i $sshkey pat@rpi4-19a.findley.cc "sudo dd if=/dev/sda bs=10M" | wsl gzip -c > $rpi4img

# Delete all but the three newest files
foreach ($rpi in $rpis) {
    $images = "$targetdir$rpi*.img.gz"
    Get-ChildItem $images | Where-Object { -not $_.PsIsContainer } | sort CreationTime -desc | 
    Select-Object -Skip 3 | Remove-Item -Force
}






<#
#!/bin/bash
BASEDIR="/mnt/rdm3/DATA/backup/"
KEEPLAST=4
#set -x
function backup {
rpiname="$1"
ping -c 3 $rpiname || return
IMG=$BASEDIR$rpiname"-$(date +%F).img.gz"
echo $IMG
# better load host CPU with gzip!
ssh pi@$rpiname "sudo dd if=/dev/mmcblk0 bs=10M"| gzip -c>$IMG
# remove older backups
ls $BASEDIR$rpiname* -t|tail -n +"$KEEPLAST"|xargs rm
}
while [[ $# -gt 0 ]]
do
backup "$1"
shift
done
####################
gci C:\temp\ -Recurse| where{-not $_.PsIsContainer}| sort CreationTime -desc| 
    select -Skip 10| Remove-Item -Force
#>