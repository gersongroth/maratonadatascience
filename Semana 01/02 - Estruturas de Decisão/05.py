n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))

media = (n1 + n2) / 2

if media == 10.0:
    print("Aprovado com Distinção")
elif media >= 7.0:
    print("Aprovado")
else:
    print("Reprovado")