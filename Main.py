from rdkit import Chem
from rdkit.Chem import AllChem, Draw
import pandas as pd
import os

source_file = 'TestImport.csv'
SMILES_column = 1
molecule_name_column = 0

# Reading CSV & making a list of SMILES

imported_file = pd.read_csv(source_file)
smiles_col_name = list(imported_file.columns)[SMILES_column]        #identifying SMILES column
name_col_name = list(imported_file.columns)[molecule_name_column]   #identifying molecule names
smiles_list = imported_file[smiles_col_name].to_list()              #Producing a list of SMILES
name_list = imported_file[name_col_name].to_list()                  #Producing a list of names


#settings for conformer generation & MMFF iterations
ConformerNumber = 10000
MaxIterations = 500

non_converged_count = 0

for i in range(len(smiles_list)):
    mol = Chem.MolFromSmiles(smiles_list[i])
    mol_name = name_list[i]
    print(mol_name)
    mol_h = Chem.AddHs(mol)
    mol_h.SetProp('_Name', str(mol_name))
    conformer_ids = AllChem.EmbedMultipleConfs(mol_h, numConfs = ConformerNumber, useBasicKnowledge = True, enforceChirality = True, numThreads=0)
    print(len(list(conformer_ids)), ' conformers')
    MMFF_out = AllChem.MMFFOptimizeMoleculeConfs(mol_h, maxIters = MaxIterations, numThreads = 0)
    #Initialising energies
    minEnergy = 999999
    minEnergy_idx = None
    #compares minimum energy of optimisation
    for index, result in enumerate(MMFF_out):
        if result[0] == 0:
            if minEnergy > result[1]:
                minEnergy = result[1]
                minEnergy_idx = index
        if result[0] != 0:
            # if result[0] = 1 the moelcule has not convertged.
            non_converged_count =+1 
    mol_h.SetProp('Minimum Energy', str(minEnergy))
    #Outputs as an SDF file
    writer = Chem.SDWriter(str(mol_h.GetProp('_Name')) + '.sdf')
    writer.write(mol_h, confId = minEnergy_idx)
