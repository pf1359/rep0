import os
from os import listdir, system, rename
import subprocess

moviepath = "/mnt/sd/movies/kids"
statuslog = "/mnt/sd/movies/kids/status.log"
errorlog = "error.log"
os.chdir(moviepath)
movies = (os.listdir(moviepath))
mkvs = [i for i in movies if i.endswith('.mkv')]
avis = [i for i in movies if i.endswith('.avi')]
isos = [i for i in movies if i.endswith('.iso')]

for mkv in mkvs:
    log = open(errorlog, "a")
    log.write(mkv +"\n")
    subprocess.call(['ffmpeg', '-v', 'error', '-i', mkv, '-f', 'null', '2>error.log'])
    log.close()
    os.rename('error.log', mkv+'.log')

for avi in avis:
    log = open(errorlog, "a")
    log.write(avi +"\n")
    subprocess.call(['ffmpeg', '-v', 'error', '-i', avi, '-f', 'null', '2>error.log'])
    log.close()
    os.rename('error.log', avi+'.log')

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




#my_frame = 3
#subprocess.call(['ffmpeg', '-r', '10', '-i', 'frame%03d.png' % my_frame,
#    ['-r',  'ntsc', 'movie%03d.mpg' % my_frame])
#     ffmpeg -v error -i Up.mkv -f null 2>Up-error.log
# Append-adds at last 
#file1 = open("myfile.txt", "a")  # append mode 
#file1.write("Today \n") 
#file1.close() 