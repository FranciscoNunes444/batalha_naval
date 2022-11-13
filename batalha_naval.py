'''#func pc atacar
func pc definir barco // sorteia um indice , se o indice for igual a o do barco na matriz, ele atira, se acertar, i+1.
func usuario atacar
func usuario definir barco
func verificar pedaços do barco
func proximo tiro do pc
func descolar barco'''
import random


BP = 'BP'
BM = 'BM'
BG = 'BG'
print("💣 💣 💣 💣 💣 💣 💣 💣 💣 💣 BATALHA NAVAL 🚢 🚢 🚢 🚢 🚢 🚢 🚢 🚢 🚢\n ")
print(''' Você tem três navios diferentes\n BARCO PEQUENO: ocupa 2 lugares no tabuleiro e vale 2 pontos\n BARCO MÉDIO: ocupa 3 lugares no tabuleiro e vale 4 pontos\n BARCO GRANDE: ocupa 4 lugares no tabuleiro e vale 6 pontos''')
print(" ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ O SEU OPONENTE SERÁ O MR.MZR 🤖 ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️ ♣️\n")

matriz_bn = [[0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]]

for i in range(len(matriz_bn)):
    print(matriz_bn[i], sep='\n')
print('')


def definirBarco():

    linhaBp = int(
        input('''Digite o numero da linha que deseja posicionar o barco pequeno: '''))
    colunaBp = int(
        input('''Digite o numero da coluna que deseja posicionar o barco pequeno: '''))
    matriz_bn[colunaBp][linhaBp] = "🛳️"
    matriz_bn[colunaBp][linhaBp+1] = "🛳️"
    for i in range(len(matriz_bn)):
        print(matriz_bn[i], sep='\n')


while True:

    definirBarco()
