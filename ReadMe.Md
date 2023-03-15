# Conformer Generation & Minimisation
This script uses Python and the required packages are shown [below](#required-packages). 
Currently, the program is built for organic based molecules, and uses the MMFF94 as the forcefield. Inorganic molecules should not be inputted to this forcefield, as results will not be accurate. 
10,000 conformers are generated for each molecule. For large molecules, this will take computational power to run, and may take some time. To edit this code, see [below](#editing-for-large-molecules)

## Required packages
There are several required packages that for the script to run correctly. Many of these are inbuilt in Python. However, 2 external packages are required. 
* [Pandas](https://pandas.pydata.org/)
* [rdkit](https://www.rdkit.org/)

There are also 2 packages coded in locally - documentation is being built, but these will help with loading, outputting and making logging easier. 

## How to use script
Full documentation can be provided in the docs 

### Calling Script
The script can be called in the command line (or PowerShell). There should be 3 inputs (including the script), put in the following order

```
Main.Py <input_file.csv> <OutputDir>
```

* Main.Py is the main script - this should be called first
* input_file.csv is a CSV file - this should also include its directory if not in the same directory as the script. Expected input file types can be seen [below](#input-file)
* OutputDir is the output directory that can be exported to. See [below](#outputs--results) for more details.  

By removing the above line, the code can be executed in an IDE, and adding the source file location. 

```
source_file = 'TestImport.csv'
```