import os 
import zipfile
from includes.Logger import logger

#InputDir should be a directory

def compress(InputDir, OutputDir = None, FileExtension='All', ZipName = 'Data.zip'):
    '''
    Common issues are found when the input directory is not double spaced. If this occurs, place a r prior to the string. 
    Full documentation is found on the GitHub repo. 
    '''
    
    AllFiles = os.listdir(InputDir)
    if FileExtension == 'All':                  #checks filetypes
        ZipFiles = AllFiles
        logger('All files in direcotry will be zipped.')
    else:
        ZipFiles = []
        for i in range(len(AllFiles)):
            if AllFiles[i].split('.')[-1] == FileExtension:
                ZipFiles.append(AllFiles[i])
                logger('Only ' + str(FileExtension) + ' will be zipped.')
    if OutputDir == None:                       #checks output dir
        OutputDir = InputDir
        logger('No output directory specified - exporting to same directory as imports.')
    i, v = list(enumerate(OutputDir))[-1]
    if i != '\\':                               #checks if output dir has a final '\' at the end
        OutputDir = str(OutputDir) + '\\'
    compression = zipfile.ZIP_DEFLATED
    zf = zipfile.ZipFile(OutputDir + ZipName, mode = 'w')
    for file in ZipFiles:
        file_name = InputDir + '\\' + file
        zf.write(file_name, file, compress_type=compression)
        logger(str(file_name) + ' written to ' + str(ZipName))
    zf.close
    logger('Zip succesfully created with ' + str(len(ZipFiles)) + ('files. Files written to ' ) + str(ZipName) + ' in ' + str(OutputDir))