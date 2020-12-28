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
    log = open(errorlog, "w")
    
    ffmpeg_command = ["ffmpeg", "-v", "error", "-i", mkv, "-f", "null", "pipe:1"]
    pipe = subprocess.run(ffmpeg_command,
                       stderr=subprocess.PIPE,
                       bufsize=10**8)
    log.write(pipe.stderr)
    log.close()
    os.rename('error.log', mkv+'.log')

for avi in avis:
    log = open(errorlog, "w")
    
    ffmpeg_command = ["ffmpeg", "-v", "error", "-i", avi, "-f", "null", "pipe:1"]
    pipe = subprocess.run(ffmpeg_command,
                       stderr=subprocess.PIPE,
                       bufsize=10**8)
    log.write(pipe.stderr)
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

 # init command
# ffmpeg_command = ["ffmpeg", "-i", mp3_path,
#                   "-ab", "128k", "-acodec", "pcm_s16le", "-ac", "0", "-ar", target_fs, "-map",
#                   "0:a", "-map_metadata", "-1", "-sn", "-vn", "-y",
#                   "-f", "wav", "pipe:1"]

 # excute ffmpeg command
# pipe = subprocess.run(ffmpeg_command,
#                       stdout=subprocess.PIPE,
#                       stderr=subprocess.PIPE,
#                       bufsize=10**8)

 # debug
# print(pipe.stdout, pipe.stderr)
