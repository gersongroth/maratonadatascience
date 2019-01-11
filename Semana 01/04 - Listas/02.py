"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""


MAX = 10
array = []
for i in range(MAX):
    valor = float(input("Informe o número " + str(i+1) + ": "))
    array.append(valor)

for v in reversed(array):
    print(v)