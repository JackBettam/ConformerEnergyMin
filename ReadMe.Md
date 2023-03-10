Workflow currently being updated

# Which forcefield to use?
* MMFF is typically good at finding organic conformers.
* UFF is good at replicating structures across the periodic table, making it better suited for inorganic compounds. 

# Required packages
There are 3 required packages that are required for the script to run correctly:
* pandas
* rdkit
* OS

# How to use script
The script expects to have SMILES strings in the second column. If this is not the case - change the variable 'SMILES_column' to the correct column. 
The identifier is expected in the first column. Again, if this is not the case, please change the variable 'molecule_name_column'