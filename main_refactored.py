import pandas as pd
from includes.Logger import logger
from includes.ImportExport import ImportExport, TempDirGen, TempDirCleanup
from rdkit import Chem
from rdkit.Chem import AllChem, Draw

#To do:
    # DONE 1 Make readdata function
    #2 Convert mol iterator into a function
    #3 refactor the comparing minimum energy optimisations
    #4 use a with loop to close - ensure memory stability
    #5 use main() def with __name__ = __main__ check


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

data = list(ReadData(source_file))
print(data)

def GenerateConformers(ZippedData, ConformersGenerated = 10000, MaxIterations = 500):
    for name, smile in ZippedData:
        mol = Chem.MolFromSmiles(smile)
        mol_h = Chem.AddHs(mol)
        mol_h.SetProp('_Name', name)




GenerateConformers(data)
