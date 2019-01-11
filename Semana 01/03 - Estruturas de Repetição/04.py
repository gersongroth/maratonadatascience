"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""

a = 80000
taxaA = 1.03
b = 200000
taxaB = 1.015

ano = 0
while a <= b:
    a = a*taxaA
    b = b*taxaB
    ano = ano + 1
print(ano)