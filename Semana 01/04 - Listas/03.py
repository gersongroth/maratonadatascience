"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

MAX = 4
array = []
soma = 0
for i in range(MAX):
    valor = float(input("Informe a nota " + str(i+1) + ": "))
    array.append(valor)
    soma = soma + valor


for v in array:
    print(v)

media = soma/MAX

print(media)