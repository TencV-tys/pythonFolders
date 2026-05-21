
names = ['Dexter','Vincent','Mark']

with open('data.txt','w') as f:
    f.write('Names::\n')
    for name in names:
        f.write(f'{name} \n')

loaded_names = []
with open('data.txt','r') as f:
    for line in f:
        loaded_names.append(line.strip())

print(loaded_names)