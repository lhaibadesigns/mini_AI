from sklearn.naive_bayes import GaussianNB

X = [[30], [25], [20], [15]]
y = [1, 1, 0, 0]

modelo = GaussianNB()

modelo.fit(X, y)

prediccion = modelo.predict([[45]])

if prediccion[0] == 1:
	print("Predicción: Soleado")
else:
	print("Predicción: Lluvioso")
