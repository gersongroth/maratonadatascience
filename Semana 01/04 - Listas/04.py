"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

consoantes = "bcdfghjklmnpqrstvwxyz"

def isConsoante(caractere):
    return caractere in consoantes

MAX = 10
array = []
consoantesLidas = []
quantidadeconsoantes = 0
for i in range(MAX):
    caractere = input("Informe o caractere " + str(i+1) + ": ")
    array.append(caractere)
    if isConsoante(caractere):
        consoantesLidas.append(caractere)
        quantidadeconsoantes = quantidadeconsoantes + 1

print (consoantesLidas)
print  (quantidadeconsoantes)