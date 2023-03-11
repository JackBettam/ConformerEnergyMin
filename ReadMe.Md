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
* Column A is expected to be the 
