import sqlite3,csv

data = [
    ["Vincent",95],
    ["Angkol",85],
    ["Mark",75],
    ["Dexter",90],
]

with open('data.csv','w') as f:
    f.write('Names,Scores\n')
    for d in data:
        f.write(f'{d[0]},{d[1]}\n')

conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS students (name TEXT, score INTEGER)')

with open('data.csv','r') as f:
    next(f)
    for name,score in csv.reader(f):
        c.execute('INSERT INTO students (name,score) VALUES (?,?)',(name,score))

conn.commit()

c.execute("SELECT name,score FROM students WHERE score >= 80")
results = c.fetchall()
print(f"High scores: {results}")


with open('high.csv','w',newline='') as f:
    write = csv.writer(f)
    
    write.writerows(results)

conn.close()

print("Done!!")