"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""

MAX = 20
par = []
impar = []
vetor = []
for i in range(MAX):
    valor = int(input("Informe um número: "))
    vetor.append(valor)
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

print(vetor)
print(par)
print(impar)