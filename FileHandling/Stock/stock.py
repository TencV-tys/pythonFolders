import sqlite3,csv

data = [
    ["Keyboard",75,8],
    ["Monitor",200,3],
    ['Mouse',500,11]
]

with open('stock.csv','w',newline='') as f:
    write = csv.writer(f)
    write.writerow(['Name','Price','Stock'])
    write.writerows(data)

conn = sqlite3.connect('products.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS products (name TEXT, price INTEGER, stock INTEGER)')

with open('stock.csv','r') as f:
    for name,price,stock in csv.reader(f):
        c.execute('INSERT INTO products (name,price,stock) VALUES (?,?,?)',(name,price,stock))
conn.commit()

c.execute('SELECT name,price,stock FROM products WHERE stock < 10')
results = c.fetchall()
print(f'Stocks added: {results}')

with open('low_stock.csv','w',newline='') as f:
    write = csv.writer(f)
    write.writerow(['Name','Price','Stock'])
    write.writerows(results)

conn.close()

print('DONE!!')
