valor1 = int(input("Informe o primeiro número: "))
valor2 = int(input("Informe o segundo número: "))
valor3 = int(input("Informe o terceiro número: "))


if(valor2 > valor1):
    valor1,valor2=valor2,valor1
if(valor3 > valor1):
    valor1,valor3=valor3,valor1
if(valor3 > valor2):
    valor2,valor3=valor3,valor2

print(valor1)
print(valor2)
print(valor3)