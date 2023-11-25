#1
import numpy as np

#2
vector = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(vector)
print('---------------------------------' + '\n')

#3
print(len(vector))
print('---------------------------------' + '\n')

#4
print(vector.ndim)
print('---------------------------------' + '\n')

#5
print(vector.shape)
print('---------------------------------' + '\n')

#6
pares = vector[vector % 2 == 0]
print(pares)
print('---------------------------------' + '\n')

#7
vector[vector % 2 != 0] = -1
vetor_ordenado = np.sort(vector)
print(vetor_ordenado)
print('---------------------------------' + '\n')

#8
vector = np.arange(12)
matriz = vector.reshape(4, -1)
print(matriz)
print('---------------------------------' + '\n')

#9
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([2, 4, 6, 8, 10])
intersecao = np.intersect1d(a, b)
print(intersecao)
print('---------------------------------' + '\n')

#10

a = np.array([1, 2, 3, 4])
b = np.array([2, 4, 6, 8, 10])
diferenca = np.setdiff1d(a, b)
print(diferenca)
print('---------------------------------' + '\n')

#11
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([2, 4, 3, 4, 10, 6])
posicoes_iguais = np.where(a == b)[0]
print(posicoes_iguais)
print('---------------------------------' + '\n')

#12
a = np.arange(21)
itens_entre_5_e_15 = a[(a >= 5) & (a <= 15)]
print(itens_entre_5_e_15)
print('---------------------------------' + '\n')

#13
vetor_aleatorio = np.random.rand(5)
print("Vetor:", vetor_aleatorio)
maximo_valor = np.max(vetor_aleatorio)
minimo_valor = np.min(vetor_aleatorio)
print("Máx:", maximo_valor)
print("Mín:", minimo_valor)
print('---------------------------------' + '\n')

#14
matriz = np.array([[7, 8, 9],
                   [4, 5, 6],
                   [1, 2, 3]])
print(matriz)
print('---------------------------------' + '\n')

#15
matriz[:, [0, -1]] = matriz[:, [-1, 0]]
print(matriz)
print('---------------------------------' + '\n')

#16
matriz[[0, -1], :] = matriz[[-1, 0], :]
print(matriz)
print('---------------------------------' + '\n')

#17
matriz_aleatoria = np.random.uniform(1, 5, size=(7, 5))
print(matriz_aleatoria)
print('---------------------------------' + '\n')

#18
print(np.prod(matriz_aleatoria.shape))
print('---------------------------------' + '\n')

#19
matriz_aleatoria = np.random.uniform(1, 5, size=(7, 5))
print(matriz_aleatoria.ndim)
print('---------------------------------' + '\n')

#20

matriz_aleatoria = np.random.uniform(1, 5, size=(7, 5))

# Imprima a forma da matriz
print("Forma da matriz:", matriz_aleatoria.shape)
print('---------------------------------' + '\n')