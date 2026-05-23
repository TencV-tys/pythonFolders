from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


model = LinearRegression()
poly = PolynomialFeatures(degree=2)

x = [[2],[4],[6],[8],[10]]
y = [4,16,36,64,100]

x_poly = poly.fit_transform(x)

model.fit(x_poly,y)

mul = model.predict(poly.fit_transform([[4]]))


print(f'Predicted for multiply : {mul[0]}')
