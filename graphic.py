import neuron
import matplotlib.pyplot as plt

figurText = "Mean Absolute Error:" + str(neuron.mae)

plt.figure()
plt.scatter(neuron.X_test, neuron.y_test, color='blue', label='Gerçek Veri')
plt.plot(neuron.X_test, neuron.y_pred, color='red', linewidth=4 , label='tahmin')
plt.xlabel('Girdi')
plt.ylabel('Çıktı')
plt.legend()
plt.text(0.95, 0.95, figurText, horizontalalignment='right', verticalalignment='top', transform=plt.gca().transAxes)
