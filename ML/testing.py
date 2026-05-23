from sklearn.linear_model import LinearRegression

model = LinearRegression()

x = [[1],[2],[3],[4],[5]]
y=[5,10,15,20,25]

model.fit(x,y)

p = model.predict([[30]])

print(f'predicted : {p[0]}')