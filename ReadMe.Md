# Conformer Generation & Minimisation
This script uses Python and the required packages are shown [below](#required-packages). 
Currently, the program is built for organic based molecules, and uses the MMFF94 as the forcefield. Inorganic molecules should not be inputted to this forcefield, as results will not be accurate. 
10,000 conformers are generated for each molecule. For large molecules, this will take computational power to run, and may take some time. To edit this code, see [below](#editing-for-large-molecules)

## Required packages
There are 4 required packages that are required for the script to run correctly:
* pandas
* rdkit
* OS
* sys

## How to use script
### Calling Script - NOT ACTIVE YET
The script can be called in the command line (or PowerShell). There should be 4 inputs (including the script), put in the following order

```
Main.Py <input_file.csv> <OutputDir> <ForceField>
```

* Main.Py is the main script - this should be called first
* input_file.csv is a CSV file - this should also include its directory if not in the same directory as the script. Expected input file types can be seen [below](#input-file)
* OutputDir is the output directory that can be exported to. See [below](#outputs--results) for more details. 
* ForceField is not currently changeable - anyn value can be placed here currently. Future implementation will include other forcefields. 


### Input file
An expected type of file is shown in the 'TestImport.csv'. 2 columns are required:
* Column A is expected to be the name of the molecule (or an identifier from a library)
* Column B is expected to be the SMILES string of the molecule. 

SDF files are not automatically compatable with this script. 
To edit which columns are which, find and edit the code to the relevent columns.

```
SMILES_column = 1
molecule_name_column = 0
```

### Editing for large molecules
If the molecule being examined is long, the generation of 10,000 conformers will likely take a long to complete. Thids is worse if the molecule library is large, and contains multiple large molecules. To edit the number of conformers, and iterations in the optimisation step, edit the following code. At least 100 conformers should be generated, and at least 500 iterations should be used. 

```
ConformerNumber = 10000
MaxIterations = 500
```

### Outputs & Results
Currently, for each molecule in the import file, a SDF file will be exported with the molecule name,  minimum energy properties, and coordinates for the minimum energy.
This can hence create a large number of SDF files and as such, it is recommended that a seperate output directory is specified to ensure that the root directory does not get clogged up. 
In future commits, the code will likely include a function to zip these conformers, and also include a CSV of the outputted properties. 