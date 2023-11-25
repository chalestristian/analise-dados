#1
import numpy as np
import pandas as pd
#2
caminho_arquivo = 'dataset/fifa.csv'
dados_temporarios = np.genfromtxt(caminho_arquivo, delimiter=',', encoding='UTF-8', dtype=None, names=True, skip_header=1)
dados = np.array([tuple(fila.tolist()[1:]) for fila in dados_temporarios])

#3
num_linhas = dados.shape[0]
print("Número de linhas lidas:", num_linhas)
print('======================================= \n')

#4
print("Número dimensões: ", dados.ndim)
print('======================================= \n')

#5
print("Forma da variável dados:", dados.shape)
print('======================================= \n')

#6
print("Dados:", dados[2, 3])
print('======================================= \n')

#7
print("Dados:", dados[0])
print('======================================= \n')

#8
print("Dados:", dados[:5])
print('======================================= \n')

#9
print("Dados:", dados[:, 0])
print('======================================= \n')

#10
print("Dados:", dados[:, 1].astype(int))
print('======================================= \n')

#11
print("Dados:", np.mean(dados[:, 1].astype(int)))
print('======================================= \n')

#12
print("Dados:", np.max(dados[:, 1].astype(int)))
print('======================================= \n')

#13
print("Dados:", np.min(dados[:, 1].astype(int)))
print('======================================= \n')

#14
idades = dados[:, 1].astype(int)
maior_idade = np.max(idades)
mascara_maior_idade = idades == maior_idade
jogadores_maior_idade = dados[mascara_maior_idade]
num_linhas_maior_idade = len(jogadores_maior_idade)
print("Dados:", num_linhas_maior_idade)
print('======================================= \n')

#15
idades = dados[:, 1].astype(int)
menor_idade = np.min(idades)
mascara_maior_idade = idades == menor_idade
jogadores_maior_idade = dados[mascara_maior_idade]
num_linhas_maior_idade = len(jogadores_maior_idade)
print("Dados:", num_linhas_maior_idade)
print('======================================= \n')

#16
dados = pd.read_csv(caminho_arquivo)
print("Dados:",  dados[dados['nacionalidade'].str.encode('utf-8') == b'Brasil'])
print('======================================= \n')

#17
print("Dados:",  len(dados[dados['nacionalidade'].str.encode('utf-8') == b'Brasil']))
print('======================================= \n')

#18
media_idade = dados['idade'].mean()
mediana_idade = dados['idade'].median()
max_idade = dados['idade'].max()
min_idade = dados['idade'].min()

media_altura = dados['altura_cm'].mean()
mediana_altura = dados['altura_cm'].median()
max_altura = dados['altura_cm'].max()
min_altura = dados['altura_cm'].min()

media_peso = dados['peso_kg'].mean()
mediana_peso = dados['peso_kg'].median()
max_peso = dados['peso_kg'].max()
min_peso = dados['peso_kg'].min()

# Imprima os resultados
print("Para a coluna 'idade':")
print("Média:", media_idade)
print("Mediana:", mediana_idade)
print("Máximo:", max_idade)
print("Mínimo:", min_idade)

print("\nPara a coluna 'altura':")
print("Média:", media_altura)
print("Mediana:", mediana_altura)
print("Máximo:", max_altura)
print("Mínimo:", min_altura)

print("\nPara a coluna 'peso':")
print("Média:", media_peso)
print("Mediana:", mediana_peso)
print("Máximo:", max_peso)
print("Mínimo:", min_peso)
print('======================================= \n')

#19
dados_brasil = dados[dados['nacionalidade'].str.encode('utf-8') == b'Brasil']
desvio_padrao_reputacao_brasil = dados_brasil['reputacao'].std()
print('Dados: ', desvio_padrao_reputacao_brasil)
print('======================================= \n')

#20
dados_brasil = dados[dados['nacionalidade'].str.encode('utf-8') == b'Brasil']
jogador_menor_potencial = dados_brasil.loc[dados_brasil['potencial'].idxmin()]
print('Dados: ', jogador_menor_potencial)
print('======================================= \n')