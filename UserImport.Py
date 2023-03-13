import sys

if len(sys.argv) != 4:
    print('Error. Could not specified inputs correctly. Expected Main.py <input csv>, <molecular forcefield>, <output directory>')
else:
    source_file = sys.argv[1] 
    forcefield = sys.argv[3]    #not currently used
    output_dir = sys.argv[2]    #not currently used 
