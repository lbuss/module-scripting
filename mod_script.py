import re
from utils import chem_spider

filename = 'inputs.txt'

lines = tuple(open(filename, 'r'))

smiles = []

for line in lines:
    if line:
        line.strip(' ')
        chem = chem_spider.get_smiles(line)
        if chem:
            smiles.append(chem)

smiles_text = '\n'.join(smiles)
smile_file = open('SMILES.txt', 'w')
smile_file.write(smiles_text)
smile_file.close

# Batch process
# kedsummary.txt
