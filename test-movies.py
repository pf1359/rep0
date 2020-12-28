import os
from os import listdir, system

path = "/mnt/sd/movies"
movies = (os.listdir(path))
mkvs = [i for i in movies if i.endswith('.mkv')]
avis = [i for i in movies if i.endswith('.avi')]
isos = [i for i in movies if i.endswith('.iso')]
print(mkvs)
print ("avis")
print (avis)
print ("isos")
print (isos)