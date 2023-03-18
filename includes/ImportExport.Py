import sys
import os
from includes.Logger import logger

def ImportExport(input):
    #logging user inputs
    UserInputs = []
    for i in range(len(input)):
        UserInputs.append(input[i])
    logger(str(UserInputs))

    # checks the user inputs for correct files
    if len(input) == 1:
        print('Error: No input file. Please add an input file.')
        logger('No input file specified. Aborted.')
        sys.exit()
    elif len(input) == 2:
        print('Information: output directory not specified. Will check if default output direcotry exists and create new one.')        
        source_file = input[1] 
        logger('Input file specified as ' + str(source_file))
        output_dir = 'output/'
        logger('Output directory not specified. Outputting to ' + str(output_dir))
    elif len(input) > 3:
        print('Warning: more inputs added. This may cause errors')
        logger('Multiple unexpected inputs. Attempting parsing.')
        source_file = input[1] 
        logger('Input file specified as ' + str(source_file))
        output_dir = input[2] 
        logger('Output directory specified as ' + str(output_dir))
    else:
        source_file = input[1] 
        logger('Input file specified as ' + str(source_file))
        output_dir = input[2] 
        logger('Output directory specified as ' + str(output_dir))

    #checks input file and if output firectory exists
    if source_file.split('.')[-1] != 'csv':
        print('Only a CSV File can be used as an import file')
        logger('Input file not a CSV. Aborted')
        sys.exit()
    else:
        logger('File is CSV.')

    if os.path.exists(output_dir) == False:
        os.mkdir(output_dir)
        logger('Made output directory')
    else:
        logger('Output directroy already exists')

    #generating temp dir
    
    return source_file, output_dir

def TempDirGen(tempdir = '__temp__'):
    if os.path.exists(tempdir) == False:
        os.mkdir(tempdir)
        logger('Made temporary directory')
    else:
        logger('Temporary directory already exists')
    return tempdir

def TemDirCleanup(tempdir = '__temp__'):
    '''
    This will first delete all files in a given directory, and then delete the directory.
    '''
    files_deleted = []
    if os.path.exists(tempdir) == True:
        for i in os.listdir(tempdir):
            file = tempdir + '/' + i
            if os.path.isfile(file) == True:
                files_deleted.append(file)
                logger('Deleted: ' + str(file))
                os.remove(file)
    logger('Deleted: ' + str(tempdir))
    os.rmdir(tempdir)
    return files_deleted