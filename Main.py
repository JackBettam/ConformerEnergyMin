from rdkit import Chem
from rdkit.Chem import AllChem, Draw
import pandas as pd
import sys
from includes.ImportExport import ImportExport, TempDirGen, TemDirCleanup
from includes.Logger import logger

#source_file, output_dir = ImportExport(sys.argv)

source_file = 'TestImport.csv'
SMILES_column = 1
molecule_name_column = 0

# Reading CSV & making a list of SMILES
imported_file = pd.read_csv(str(source_file))
logger(str(source_file) + ' read succesfully')
smiles_col_name = list(imported_file.columns)[SMILES_column]        #identifying SMILES column
name_col_name = list(imported_file.columns)[molecule_name_column]   #identifying molecule names
smiles_list = imported_file[smiles_col_name].to_list()              #Producing a list of SMILES
name_list = imported_file[name_col_name].to_list()                  #Producing a list of names
df =[]                                                              #Empty dataframe to append into

#settings for conformer generation & MMFF iterations
ConformerNumber = 10000
MaxIterations = 500

#non-converged molecules
non_converged_count = 0

for i in range(len(smiles_list)):
    mol = Chem.MolFromSmiles(smiles_list[i])
    mol_name = name_list[i]
    mol_h = Chem.AddHs(mol)
    mol_h.SetProp('_Name', str(mol_name))
    logger(str( mol_h.GetProp('_Name')) + ' succesfully read.')
    print('Testing: ', mol_h.GetProp('_Name'))
    
    #embedding molecule and generating conformers 
    conformer_ids = AllChem.EmbedMultipleConfs(mol_h, numConfs = ConformerNumber, useBasicKnowledge = True, enforceChirality = True, numThreads=0)
    logger(str( mol_h.GetProp('_Name')) + ' succesfully embedded with ' + str(ConformerNumber) + ' conformers.')
    MMFF_out = AllChem.MMFFOptimizeMoleculeConfs(mol_h, maxIters = MaxIterations, numThreads = 0)
    logger(str( mol_h.GetProp('_Name')) + ' succesfully optimised.')

    
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
            # if result[0] = 1 the moelcule has not converged
            non_converged_count =+1
            print('Warning:', mol_h.GetProp('_Name'), 'could not converged')
            logger(str( mol_h.GetProp('_Name')) + ' failed to converge.')
    mol_h.SetProp('Minimum Energy ', str(minEnergy))
    logger(str( mol_h.GetProp('_Name')) + ' succesfully energy minimised.')

   
    #Outputs as an SDF file
    temp_dir = TempDirGen()
    file_name = str(temp_dir) + '/' + str(mol_h.GetProp('_Name') + '.sdf') #outputting to a temp directory
    writer = Chem.SDWriter(file_name)
    writer.write(mol_h, confId = minEnergy_idx)
    writer.flush()
    writer.close()
    logger(str( mol_h.GetProp('_Name')) + ' outputted as ' + str(file_name))

    #Appending data to dataframe
    df_data = [str(mol_h.GetProp('_Name')), str(smiles_list[i]), str(minEnergy)]
    df.append(df_data)

    print('Successfully tested: ', mol_h.GetProp('_Name'))

#Creating formal dataframe
df = pd.DataFrame(df, columns=['ID', 'SMILES', 'Minimum energy'])
print(df)
print('Number of non-converged molecules: ', non_converged_count)

print(TemDirCleanup())