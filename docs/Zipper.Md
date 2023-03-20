# Zipper.py
Zipper takes in a directory (temporary in this case), copies and then zips up those copied files, and outputs it to another directory. Please ensure that the note on strings is read below. 

## Included functions
There is one function in this package. 

### compress
Called by:
```
from includes.Zipper import compress
compress(InputDir, OutputDir, FileExtension, ZipName)
```

The only mandatory input is ```InputDir``` which is directory of the files that are to be compressed. 

Optional variables to call are:
* ```OutputDir``` is called to place the resulting zip file in a directory. If no ```OutputDir``` is specified, it will output the zip to the ```InputDir```.
* ```FileExtension``` is to specify which file types should be zipped. Filetype should be specified as a string, with no full stop (i.e. ```txt``` __not__ ```.txt```) If no ```FileExtension``` is specified, then all fieltypes will be zipped. 
* ```ZipName``` is the name of the new Zip that is created. Please ensure that the zip extension is created, or an extensionless zip is created. This defaults to ```'Data.zip'```. 

## Pre-required packages
This requires the following packages from standard installs of Python:
* os
* zipfile

Additionally [logger](/docs/Logger.Md) is used.

If running in the same directory as Main.Py, the import section will not need 'includes'. 