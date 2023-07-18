import printData
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#printData.py den verileri çektim
values = printData.values
#Verileri Numpy Array'ına çevirdim
values = np.array(values).astype(float)

def make_prediction(X, y, next_value):
    #Bir LinearRegression modeli oluşturdum
    model = LinearRegression()
    #
    model.fit(X, y)
    #
    next_prediction = model.predict(next_value)
    return next_prediction

X = values.reshape(-1, 1)
y = 5 * X + np.random.randn(len(values), 1)
next_value = X[-1] + 0.1
next_value = np.array([next_value]).reshape(1, -1)
prediction = make_prediction(X, y, next_value)
print("Bir sonraki tahmin edilen değer:", prediction)
estimateValue = "Tahmin Edilen Sonraki Değer: " + str(prediction)
plt.text(0.95, 0.02, estimateValue, horizontalalignment='right', verticalalignment='bottom', transform=plt.gca().transAxes, fontsize=12, color='purple')

plt.show()
