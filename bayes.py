import numpy as np
import math
import matplotlib.pyplot as plt
import random

# primero 
def gauss(sigma, N):
    x = np.genfromtxt('valores.txt')
    resultado = np.zeros(len(x))
    for i in range(len(x)):
        probn = (1 / sigma * np.sqrt(2 * math.pi))*np.exp(-0.5 *(x[i]**2 / sigma**2))
        if (probn >= np.random.random()):
            resultado[i] = probn

    return (resultado)


a = gauss(60, 100000)

#plt.plot(x, hola)
plt.hist(a, density=True)
plt.title('el valor medio de estos valores y su desviacion estandar')
plt.xlabel('valor medio')
plt.ylabel('desviacion estandar')
plt.savefig("sigma.png")

#segundo 

h = np.genfromtxt('monthrg.dat')
x = np.transpose(h)


def FOUR(X):

    N = len(X)
    i = 1j
    Y = np.zeros(N)

    for n in range(N):
        sumatoria = 0
        for k in range(N):
            tota = X[k] * np.exp(-2 * np.pi * i * k * n / N)
            sumatoria += abs(tota)

        Y[n] = sumatoria / N
    return Y


manchas = x[3]
tiempo = x[2]
#periodo
anos = x[0]
periodo = []
sumatoria = 1
for i in range(len(anos) - 1):
    if (anos[i] == anos[i + 1]):
        sumatoria += 1
    else:
        sumatoria = 0

periodo.append(sumatoria)
print('el periodo en unidades de anio son', periodo)

plt.figure()
plt.subplot(2, 2, 1)
plt.plot(manchas, tiempo)
plt.subplot(2, 2, 1)
a = FOUR(tiempo)
plt.stem(manchas, a)

plt.savefig("solar.png")