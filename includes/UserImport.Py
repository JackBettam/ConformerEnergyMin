import sys
import os
from Logger import initiate_log, logger


log = initiate_log()

output_dir = None

if len(sys.argv) != 4:
    print('Error. Could not specified inputs correctly. Results may not be correct. See log for more details. Expected Main.py <input csv>, <molecular forcefield>, <output directory>')
else:
    source_file = sys.argv[1] 
    forcefield = sys.argv[3]    #not currently used
    output_dir = sys.argv[2]    #not currently used 

if output_dir == None:
    output_dir = 'output/'
    logger(log, 'Output directory not specified.')

#if os.path.exists(output_dir) == False:
    #os.mkdir(output_dir)