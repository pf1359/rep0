import os
import datetime
import glob

path = "/opt/storage/backup"

today = datetime.datetime.today()
os.chdir(path)

for root,directories,files in os.walk(path,topdown=False):
    for name in files:
        t = os.stat(os.path.join(root, name)) [8]
        filetime = datetime.datetime.fromtimestamp(t) - today

        if filetime.days <= -60:
            os.remove(os.path.join(root, name))
