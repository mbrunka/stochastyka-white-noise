import numpy as np
import matplotlib.pyplot as plt

# Parametry sygnału
czas_trwania = 1  # sekundy
czestotliwosc_probkowania = 1000  # Hz

# Wygenerowanie szumu białego
liczba_probek = czas_trwania * czestotliwosc_probkowania
szum_bialy = np.random.uniform(-1, 1, liczba_probek)

# Wykres czasowy
czas = np.linspace(0, czas_trwania, liczba_probek)
plt.figure(figsize=(10, 5))
plt.plot(czas, szum_bialy)
plt.title('Wykres czasowy szumu białego o rozkładzie równomiernym')
plt.xlabel('Czas [s]')
plt.ylabel('Amplituda')
plt.grid(True)
plt.show()

# Wykres częstotliwościowy
spektrum = np.abs(np.fft.fft(szum_bialy))[:liczba_probek//2]
czestotliwosc = np.linspace(0, czestotliwosc_probkowania/2, len(spektrum))
plt.figure(figsize=(10, 5))
plt.plot(czestotliwosc, spektrum)
plt.title('Wykres częstotliwościowy szumu białego o rozkładzie równomiernym')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda')
plt.grid(True)
plt.show()

