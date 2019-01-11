valor1 = float(input("Informe o valor do primeiro produto: "))
valor2 = float(input("Informe o valor do segundo produto: "))
valor3 = float(input("Informe o valor do terceiro produto: "))


if(valor1 > valor2):
    valor1,valor2=valor2,valor1
if(valor1 > valor3):
    valor1,valor3=valor3,valor1

print("Menor:",valor1)