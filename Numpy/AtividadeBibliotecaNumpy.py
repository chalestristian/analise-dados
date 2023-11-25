import numpy as np

ExA = np.array([[12, 9, 4, 1],
                 [11, 5, 8, 1],
                 [1, 2, 3, 1]])

ExB = np.array([[1, 5],
                 [1, 7],
                 [1, 9],
                 [1, 1]])

#print('ExA: \n', ExA, '\n', 'ExB: \n', ExB)

ExC = np.dot(ExA, ExB)
#print("ExC: \n", ExC)

def calcular_estatisticas_matriz(matriz):
    media_linhas = np.mean(matriz, axis=1)
    desvio_padrao_linhas = np.std(matriz, axis=1)
    media_colunas = np.mean(matriz, axis=0)
    desvio_padrao_colunas = np.std(matriz, axis=0)
    return media_linhas, desvio_padrao_linhas, media_colunas, desvio_padrao_colunas
ExC = np.dot(ExA, ExB)
media_linhas, desvio_padrao_linhas, media_colunas, desvio_padrao_colunas = calcular_estatisticas_matriz(ExC)

#print("Média das Linhas:", media_linhas)
#print("Desvio Padrão das Linhas:", desvio_padrao_linhas)
#print("Média das Colunas:", media_colunas)
#print("Desvio Padrão das Colunas:", desvio_padrao_colunas)

ExD = ExA[:, -2:]
media_ExD = np.mean(ExD)
print("ExD:")
print(ExD)
print("\nMédia de ExD:", media_ExD)