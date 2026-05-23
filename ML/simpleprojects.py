from sklearn.linear_model import LinearRegression

x = [[100],[200],[300],[400],[500]]
y = [10,20,30,40,50]

model = LinearRegression()
model.fit(x,y)
p = model.predict([[750]])
print(f'Predicted price for: {p[0]}')
print(f'Formula is Price X {model.coef_[0]:,.1f}')
