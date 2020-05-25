#!/bin/bash

#Created 23May2020,ptf

rsync -av --delete /home/ /media/1tb/backups/home
rsync -av --delete /etc/ /media/1tb/backups/etc
rsync -av --delete --exclude '/root/exclude.txt' /var/ /media/1tb/backups/var
rsync -av --delete /root/ /media/1tb/backups/root

#cd /media/1tb/archive && zip -r "archive-$(date +"%Y-%m-%d").zip" /media/1tb/backups/ -x /media/1tb/backups/var/run/speech-dispatcher/\*
#timestamp= $( date +%y-%m-%d-%H_%M)
#name="(date +"%y-%m-%d")"
cd /media/1tb/archive && tar -zcvf $( date '+%y-%m-%d-%H_%M' ).tar.gz /media/1tb/backups

find /media/1tb/archive -name "*.tar.gz" -type f -mtime +30 -exec rm -f {} \;
