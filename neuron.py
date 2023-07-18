import joblib
import printData
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

values = printData.values
values = [float(value) for value in values]
values = np.array(values)

X = np.array(values).reshape(-1, 1)
y = 5 * X + np.random.randn(len(values), 1)

df = pd.DataFrame({'Girdi': X.flatten(), 'Çıktı': y.flatten()})

X_train, X_test, y_train, y_test = train_test_split(df[['Girdi']], df['Çıktı'], test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)

joblib.dump(values, 'learnData.pkl')
loadedValues = joblib.load('learnData.pkl')

for i in range(len(loadedValues)):
    print("Tarih: " + str(epoch.dates[i]) + " Girdi: " + str(loaded_values[i]) + " Çıktı: " + str(y[i]))
print("Hata Payı (Mean Absolute Error):", mae)