import os
from datetime import datetime

file_Exist = os.path.isfile('log.txt')

if os.path.isfile('log.txt') == False:
    log = open('log.txt', 'w+')
    log.write(str(str(datetime.now().isoformat(' ', 'seconds')) + ': Created log file'))
    log.close()