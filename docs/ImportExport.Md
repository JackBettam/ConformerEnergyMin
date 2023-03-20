# ImportExport.py
This local package is used to import molecules and export files. It moves a lot of logic from the main script to this package to make the main script easier to understand. 

This package also uses the local [Logger](/docs/Logger.Md) package which records errors and unespected codes, as well as repeats what is defined by the user. 

## Included functions
There are three functions within the package. Each are below with documentation on how to use each function:

### ImportExport
Called by:

```
from includes.ImportExport import ImportExport
source_file, output_dir = ImportExport(sys.argv)
```

This takes the user input from the command line when running the script. This should only be used when running the script from a command line. If using an IDE use the command below.

A check occurs to ensure that the output_dir is specified, and if not specified then a default output directory of 'output' is used. This will also create a directory if one does not exist already. A check also occurs if the input file (source_file) is a CSV. This does not check column data. CSV files should be in an appropiate format, discussed more [here](/docs/Main.Md)

If Main.py is ran in an IDE, then the script should bypass this line, and then call in main.py. This bypasses the check for an outoput directory, and as such the user will need to create one manually, and assign it to output_dir. 

```
source_file, output_dir = 'TestImport.csv', 'output'
```

### TempDirGen
Called by:
```
from includes.ImportExport import TempDirGen
temp_dir = TempDirGen()
```

This creates a directory called ```__Temp__``` 

