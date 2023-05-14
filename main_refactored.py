import pandas as pd
from includes.Logger import logger
from includes.ImportExport import ImportExport, TempDirGen, TempDirCleanup
from rdkit import Chem
from rdkit.Chem import AllChem, Draw
from includes.Zipper import compress


#To do:
    # DONE 1 Make readdata function
    # DONE 2 Convert mol iterator into a function
    # DONE 3 refactor the comparing minimum energy optimisations
    #4 use a with loop to close - ensure memory stability
    #5 use main() def with __name__ = __main__ check
    #6 Document fully with examples all of the functions used


source_file, output_dir = 'TestImport.csv', 'output'       #IDE only

def ReadData(InputFile):
    imported_file = pd.read_csv(str(InputFile))
    logger(str(InputFile) + ' read succesfully')
    SMILES_column, molecule_name_column = 1, 0
    smiles_col_name = list(imported_file.columns)[SMILES_column]       
    name_col_name = list(imported_file.columns)[molecule_name_column]  
    smiles_list = imported_file[smiles_col_name].to_list()              
    name_list = imported_file[name_col_name].to_list()
    result = zip(name_list, smiles_list)
    logger(str(InputFile) + ' columns zipped succesfully. Returning to caller function.')                  
    return result

data = ReadData(source_file)

def GenerateMolWithH(ZippedData):
    df = []
    for name, smile in ZippedData:
        #Converting to molecule with hydrogens and naming
        mol = Chem.MolFromSmiles(smile)
        mol_h = Chem.AddHs(mol)
        mol_h.SetProp('_Name', name)
        logger(str( mol_h.GetProp('_Name')) + ' succesfully read and added to list.')
        df.append(mol_h)
    logger("Zip succesfully read and imported 1D dataframe. Returning back to caller.")
    return df

def GenerateConformers(ZippedData, ConformersGenerated = 10000, MaxIterations = 500):
    logger("Sending zipped data to GenerateMolWithH function.")
    MolsWithH = GenerateMolWithH(ZippedData)
    StoredEnergies = []
    #df should contain Mol with H and their name as a prop
    #print(type(df))
    for i in MolsWithH:
        print("Calculating Energies for", i.GetProp('_Name'))
        AllChem.EmbedMultipleConfs(i, numConfs=ConformersGenerated, useBasicKnowledge = True, enforceChirality = True, numThreads=0)
        logger(str( i.GetProp('_Name')) + ' succesfully embedded with ' + str(ConformersGenerated) + ' conformers.')
        MMFF_out = AllChem.MMFFOptimizeMoleculeConfs(i, maxIters = MaxIterations, numThreads = 0)
        logger(str( i.GetProp('_Name')) + ' succesfully optimised.')
        StoredEnergies.append(MMFF_out)
    return MolsWithH, StoredEnergies

def MinimimEnergySelection(Mol, StoredEnergies):
    df = []
    for OuterIndex, MolEnergyData in enumerate(StoredEnergies):
        #Outer loop looks at the indivdual molecules
        minEnergyIndex = 0
        minEnergyValue = MolEnergyData[minEnergyIndex][1]
        #Comparing against all value in list from MMFF Output
        for index, MMFFOut in enumerate(MolEnergyData):
            CurrentEnergy = MMFFOut[1]
            if CurrentEnergy < minEnergyValue:
                minEnergyValue = CurrentEnergy
                minEnergyIndex = index
        Mol[OuterIndex].SetProp('Minimum Energy', str(minEnergyValue))
        logger(str( Mol[OuterIndex].GetProp('_Name')) + ' succesfully energy minimised.')
        print(Mol[OuterIndex].GetProp('_Name'), 'minimised with an energy of', minEnergyValue)
        dfData = [Mol[OuterIndex], minEnergyIndex]
        df.append(dfData)
    return df


def Writer(array, output_directory):
    temp_dir = TempDirGen()
    for entry in array:
        mol_h = entry[0]
        minEnergyIndex = entry[1]
        FileName = str(temp_dir) + '/' + str(mol_h.GetProp('_Name') + '.sdf')
        writer = Chem.SDWriter(FileName)
        writer.write(mol_h, confId = minEnergyIndex)
        writer.flush()
        writer.close()
        logger(str( mol_h.GetProp('_Name')) + ' outputted as ' + str(FileName))
    compress('__temp__', output_directory, 'sdf', 'SDF Files2.zip')
    TempDirCleanup()

mol, df = GenerateConformers(data)
data2 = MinimimEnergySelection(mol, df)

Writer(data2, output_dir)