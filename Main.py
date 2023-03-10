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
name_list = imported_file[name_col_name].to_list()                #Producing a list of names


for i in range(len(smiles_list)):
    mol = Chem.MolFromSmiles(smiles_list[i])
    mol_name = name_list[i]
    #print(mol_name)
    drawer = Draw.rdMolDraw2D.MolDraw2DCairo(300,300)
    drawer.DrawMolecule(mol, legend=mol_name)
    drawer.FinishDrawing()
    drawer.WriteDrawingText(str(mol_name)+'.png')