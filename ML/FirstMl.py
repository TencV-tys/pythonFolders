from sklearn.linear_model import LinearRegression

x = [[500],[1000],[1500],[2000],[2500]]
y = [80000,150000,220000,290000,360000]

model = LinearRegression()
model.fit(x,y)
p = model.predict([[1800]])

print(f'Predicted data: {p[0]:,.1f}')
print(f'formula price x {model.coef_[0]:,.1f}')