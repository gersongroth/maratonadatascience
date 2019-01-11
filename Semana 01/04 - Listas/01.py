"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""

MAX = 5
array = []
for i in range(MAX):
    valor = int(input("Informe o número " + str(i+1) + ": "))
    array.append(valor)

for v in array:
    print(v)