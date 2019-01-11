"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""

ladoA = int(input("Informe o lado A do triângulo: "))
ladoB = int(input("Informe o lado B do triângulo: "))
ladoC = int(input("Informe o lado C do triângulo: "))

if ladoB>ladoA:
    ladoA,ladoB=ladoB,ladoA
if ladoC > ladoA:
    ladoA, ladoC = ladoC, ladoA
if ladoC > ladoB:
    ladoB, ladoC = ladoC, ladoB

if (ladoB + ladoC) > ladoA:
    if(ladoA == ladoB and ladoA == ladoC):
        print("equilátero")
    elif ladoA == ladoB or ladoB==ladoC:
        print("isósceles")
    else:
        print("escaleno")