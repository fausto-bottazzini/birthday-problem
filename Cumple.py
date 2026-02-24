import numpy as np
import matplotlib.pyplot as plt
import random as rm

# N= personas
# M = esp
# S = seed

# M=int(input("Número de experimentos:"))
# S=(input("Seed:"))

S=482
rm.seed(S)

def nac(N):
    return [rm.randint(1,365) for _ in range(N)]
def coin(list):
    return len(set(list))<len(list)
def prop(N,M):
    resultado = [nac(N) for _ in range(M)]
    probabilidad = (np.sum(coin(x) for x in resultado))/M
    return probabilidad

M=10000

Nmax=70
plt.figure()
plt.title("Probabilidad de que alguien cumpla el mismo dia que alguien")
plt.ylabel("Probabilidad")
plt.xlabel("Numero de personas")
plt.axhline(50.7,color = "brown", linewidth = 1, linestyle = "dashed")
# plt.axvline(23,color = "brown", linewidth = 1, linestyle = "dashed")
plt.plot(range(1,Nmax+1), [prop(a,M)*100 for a in range(1,Nmax+1)],".")

plt.show()

input("enter para reiniciar...")