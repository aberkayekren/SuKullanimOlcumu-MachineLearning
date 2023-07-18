import neuron
import printData as pd
import matplotlib.pyplot as plt

firstIndex = pd.values[0]

# Doğruluk değerine göre mesaj yazdırma
accuracyThreshold = 0.1  # Doğruluk eşiği
accuracy = 1 - neuron.mae
if all(index == firstIndex for index in pd.values):
    plt.text(0.5, 0.1, "Su Tüketimi Yanlış | Sabit Olamaz", horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12, color='red')
    print("Su Tüketimi Yanlış | Sabit Olamaz")

elif accuracy >= accuracyThreshold:
    plt.text(0.5, 0.1, "Su Tüketimi Doğru", horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12, color='green')
    print("Su Tüketimi Doğru")
else:
    plt.text(0.5, 0.1, "Su Tüketimi Yanlış", horizontalalignment='center', verticalalignment='center', transform=plt.gca().transAxes, fontsize=12, color='red')
    print("Su Tüketimi Yanlış | Hata Payı Çok")