import os
from datetime import datetime

def logger(message, file='log.txt'):
    if  os.path.isfile(file) == False:
        log = open(file, 'w+')
        now = datetime.now().isoformat(' ', 'seconds')
        log.write(str(now) + ': Created log file.')
        log.write('\n')
        log.close()
    now = datetime.now().isoformat(' ', 'seconds')
    log = open(file, 'a')
    log.write(str(now) + ': ' + str(message))
    log.write('\n')
    log.close()
