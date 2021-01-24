import os
import tarfile
import logging
import time

timestr = time.strftime("%Y%m%d-%H%M%S")
backuptargets = ['/opt/minecraftdir/']
backupdest = '/opt/storage/backup/'

logging.basicConfig(filename = os.path.join(backupdest, timestr+'tar_error.log'), level = logging.INFO)
for directory in backuptargets:
    try:
        full_dir = os.path.join(directory)
        targz = tarfile.open(os.path.join(backupdest, directory, timestr+'.tar.gz'), 'w:gz')
        targz.add(full_dir)
        targz.close()
        
    except Exception as e:
        logging.exception (str(e))