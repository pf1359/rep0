rsync -av -delete --exclude-from='/root/exclude-file.txt' / /media/1tb/rpi4

zip --password PASSWORD /media/1tb/rpi4-$(date +"%Y-%m-%d-%h").zip /media/1tb/rpi4/

find /var/log -name "*.zip" -type f -mtime +30 -exec rm -f {} \;

rm -rf /media/1tb/rpi4/*
