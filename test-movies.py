import os
from os import listdir, system, rename
import subprocess
import ffmpeg
from ffmpeg import Error

moviepath = "/mnt/sd/movies/kids"
statuslog = "/mnt/sd/movies/kids/status.log"
errorlog = "error.log"

os.chdir(moviepath)
movies = (os.listdir(moviepath))
mkvs = [i for i in movies if i.endswith('.mkv')]
avis = [i for i in movies if i.endswith('.avi')]
isos = [i for i in movies if i.endswith('.iso')]

for mkv in mkvs:
    log = open(errorlog, "w")
    try:
        ffmpeg.input(mkv) \
           .output (None) \
           .run(capture_stdout=False, capture_stderr=True)
    except ffmpeg.Error as e:
        log.write('stdout:', e.stdout.decode('utf8'))
        log.write('stderr:', e.stderr.decode('utf8'))
        raise e
    log.close()

for avi in avis:
    log = open(errorlog, "w")
    try:
        ffmpeg.input(avi) \
           .output (None) \
           .run(capture_stdout=False, capture_stderr=True)
    except ffmpeg.Error as e:
        log.write('stdout:', e.stdout.decode('utf8'))
        log.write('stderr:', e.stderr.decode('utf8'))
        raise e
    log.close()


# Need to figure out how to do this for ISOs

movielogs = [i for i in movies if i.endswith('.log')]
for movielog in movielogs:
    kb = os.path.getsize(movielog)
    if kb == 0:
        logstatus = open(statuslog, "a")
        logstatus.write(kb+' had no errors.\n')
        logstatus.close()
    else:
        logstatus = open(statuslog, "a")
        logstatus.write(kb+' had errors.\n')
        logstatus.close()




