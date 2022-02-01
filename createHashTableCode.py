#Read external data
import csv
data = []
with open('exampleData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='|')
    for row in reader:
        data.append(row)

#Create preconfigured data array and initialize it
with open('declaration.st', 'w') as f:
    f.write('VAR\n')
    f.write(f'\tvHashTable : ARRAY[0..{len(data)-1}] OF REAL := [\n')
    for row in data:
        f.write(f"\t\t{row.get('Value')},\n")

    #TODO: remove last comma
    f.write('\t] (*Hash table*);\n')
    f.write('END_VAR')

#Create text based enumeration
with open('constantEnum.dt', 'w') as f:
    f.write('TYPE CNST :\n')
    f.write(f'(\n')
    for idx, row in enumerate(data):
        f.write(f"\t{row.get('Ident')} := {idx}, (*{row.get('Text name')}*)\n")

    #TODO: remove last comma
    f.write(') UINT;\nEND_TYPE')

#Create code calls
with open('code.st', 'w') as f:
    for idx, row in enumerate(data):
        f.write(f"vHashTable[{row.get('Ident')}];\n")
