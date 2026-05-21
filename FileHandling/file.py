with open('test.txt','w') as f:
    f.write('Hello ML!')

with open('test.txt','r') as f:
    content = f.read()
    print(content)

with open('test.txt','a') as f:
    f.write('\n New Line')

import csv 

with open('test.csv','w',newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(['name','age'])
    writer.writerow(['Vincent',23])
    
with open('test.csv','r') as f: 
    reader = csv.reader(f)
    for r in reader:
        print(r)
