import os
import zlib
import zipfile

#InputDir should be a directory

def compress(InputDir, OutputDir = 'InputDir', FileExtension='All'):
    AllFiles = os.listdir(InputDir)
    if FileExtension == 'All':
        ZipFiles = AllFiles
    else:
        ZipFiles = []
        for i in range(len(AllFiles)):
            if AllFiles[i].split('.')[-1] == FileExtension:
                ZipFiles.append(AllFiles[i])
    
compress(r'C:\Users\jackb\OneDrive\Documents\GitHub\ConformerEnergyMin\output', FileExtension = 'sdf')