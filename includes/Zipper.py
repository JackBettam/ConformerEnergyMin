import os
import zlib
import zipfile

#InputDir should be a directory

def compress(InputDir, OutputDir = None, FileExtension='All', ZipName = 'Data.zip'):
    AllFiles = os.listdir(InputDir)
    if FileExtension == 'All':          #checks filetypes
        ZipFiles = AllFiles
    else:
        ZipFiles = []
        for i in range(len(AllFiles)):
            if AllFiles[i].split('.')[-1] == FileExtension:
                ZipFiles.append(AllFiles[i])
    if OutputDir == None:               #checks output dir
        OutputDir = InputDir
    i, v = list(enumerate(OutputDir))[-1]
    if i != '\\':
        OutputDir = str(OutputDir) + '\\'
    print(OutputDir)
    compression = zipfile.ZIP_DEFLATED
    zf = zipfile.ZipFile(OutputDir + ZipName, mode = 'w')
    for file in ZipFiles:
        #print(file)
        zf.write(InputDir + '\\' +file, file, compress_type=compression)
    

compress(r'C:\Users\jackb\OneDrive\Documents\GitHub\ConformerEnergyMin\output', FileExtension = 'sdf')
