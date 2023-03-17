import os
import zlib
import zipfile

#InputDir should be a directory

def compress(InputDir, OutputDir = None, FileExtension='All', ZipName = 'Data.zip'):
    '''
    Common issues are found when the input directory is not double spaced. If this occurs, place a r prior to the string. 
    Full documentation is found on the GitHub repo. 
    '''
    
    AllFiles = os.listdir(InputDir)
    if FileExtension == 'All':                  #checks filetypes
        ZipFiles = AllFiles
    else:
        ZipFiles = []
        for i in range(len(AllFiles)):
            if AllFiles[i].split('.')[-1] == FileExtension:
                ZipFiles.append(AllFiles[i])
    if OutputDir == None:                       #checks output dir
        OutputDir = InputDir
    i, v = list(enumerate(OutputDir))[-1]
    if i != '\\':                               #checks if output dir has a final '\' at the end
        OutputDir = str(OutputDir) + '\\'
    print(OutputDir)
    compression = zipfile.ZIP_DEFLATED
    zf = zipfile.ZipFile(OutputDir + ZipName, mode = 'w')
    for file in ZipFiles:
        #print(file)
        zf.write(InputDir + '\\' +file, file, compress_type=compression)
    

print(help(compress))