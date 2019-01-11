"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
"""


taxaA = taxaB = 0
while taxaA <= taxaB:
    a = int(input("Informe a população da cidade A"))
    taxaA = float(input("Informe a taxa de crescimento da cidade A"))
    b = int(input("Informe a população da cidade B"))
    taxaB = float(input("Informe a taxa de crescimento da cidade B"))

    if taxaA <= taxaB:
        print("Taxa de A deve ser maior que taxa de B")

ano = 0
while a <= b:
    a = a*(taxaA/100 + 1)
    b = b*(taxaB/100 + 1)
    ano = ano + 1
print(ano)