# Conformer Generation & Minimisation
This script uses Python and the required packages are shown [below](https://github.com/JackBettam/ConformerEnergyMin#required-packages). 
Currently, the program is built for organic based molecules, and uses the MMFF94 as the forcefield. Inorganic molecules should not be inputted to this forcefield, as results will not be accurate. 
10,000 conformers are generated for each molecule. For large molecules, this will take computational power to run, and may take some time. To edit this code, see [below](https://github.com/JackBettam/ConformerEnergyMin#how-to-use-script)

## Required packages
There are 3 required packages that are required for the script to run correctly:
* pandas
* rdkit
* OS

## How to use script
### Input file
An expected type of file is shown in the 'TestImport.csv'. 2 columns are required:
* Column A is expected to be the name of the molecule (or an identifier from a library)
* Column B is expected to be the SMILES string of the molecule. 

SDF files are not automatically compatable with this script. 
To edit which columns are which, find and edit the code to the relevent columns.
'''
SMILES_column = 1
molecule_name_column = 0
'''

### Editing for large molecules
If the molecule being examined is long, the generation of 10,000 conformers will likely take a long to complete. Thids is worse if the molecule library is large, and contains multiple large molecules. To edit the number of conformers, and iterations in the optimisation step, edit the following code. At least 100 conformers should be generated, and at least 500 iterations should be used. 
'''
ConformerNumber = 10000
MaxIterations = 200
'''