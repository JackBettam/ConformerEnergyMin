import sys
import os
from Logger import initiate_log, logger

#initiating log
log = initiate_log()


#logging user inputs
UserInputs = []
for i in range(len(sys.argv)):
    UserInputs.append(sys.argv[i])
logger(log, str(UserInputs))

# checks the user inputs for correct files
if len(sys.argv) == 1:
    print('Error: No input file. Please add an input file.')
    logger(log, 'No input file specified. Aborted.')
    sys.exit()
elif len(sys.argv) == 2:
    print('Information: output directory not specified. Will check if default output direcotry exists and create new one.')        
    source_file = sys.argv[1] 
    logger(log, 'Input file specified as ' + str(source_file))
    output_dir = 'output/'
    logger(log, 'Output directory not specified. Outputting to ' + str(output_dir))
elif len(sys.argv) > 3:
    print('Warning: more inputs added. This may cause errors')
    logger(log, 'Multiple unexpected inputs. Attempting parsing.')
    source_file = sys.argv[1] 
    logger(log, 'Input file specified as ' + str(source_file))
    output_dir = sys.argv[2] 
    logger(log, 'Output directory specified as ' + str(output_dir))
else:
    source_file = sys.argv[1] 
    logger(log, 'Input file specified as ' + str(source_file))
    output_dir = sys.argv[2] 
    logger(log, 'Output directory specified as ' + str(output_dir))

#checks input file and if output firectory exists
if source_file.split('.')[-1] != 'csv':
    print('Only a CSV File can be used as an import file')
    logger(log, 'Input file not a CSV. Aborted')
    sys.exit()
else:
    logger(log, 'File is CSV.')

if os.path.exists(output_dir) == False:
    os.mkdir(output_dir)
    logger(log, 'Made output directory')
else:
    logger(log, 'Output directroy already exists')