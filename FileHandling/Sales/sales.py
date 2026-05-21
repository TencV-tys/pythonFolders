import sqlite3,csv

data = [
["Laptop",1000,2],
['Mouse',25,5],
['Keyboard',75,1],
['Monitor',200,1],
['Phone',500,3]
]

with open('sales.csv','w') as f:
    write = csv.writer(f)
    write.writerow(['Product','Price','Quantity'])
    write.writerows(data)

conn = sqlite3.connect('sales.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS sales (product TEXT,price INTEGER, quantity INTEGER)')

with open('sales.csv','r') as f:
    next(f)
    for product, price, quantity in csv.reader(f):
        c.execute('INSERT INTO sales (product,price,quantity) VALUES (?,?,?)',(product,price,quantity))
conn.commit()

c.execute('SELECT product,price,quantity, (price * quantity) as revenue FROM sales WHERE (price * quantity) > 200')
result = c.fetchall()
print(f'Results Adedd: {result}')

with open('big_sales.csv','w') as f:
     write = csv.writer(f)
     write.writerow(['product', 'price', 'quantity', 'revenue'])
     write.writerows(result)

conn.close()

print("Done")