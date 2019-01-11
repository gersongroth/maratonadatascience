"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""

salario = float(input("Informe o salário: R$ "))

aumento = 0
if salario <= 280.0:
    aumento = 20
elif salario < 700.0:
    aumento = 15
elif salario < 1500:
    aumento = 10
else:
    aumento = 5

valorAumento = salario * (aumento / 100)
novoSalario = salario + valorAumento

print("Salario original: R$ %.2f" % salario)
print("Porcentagem de aumento: %d%%" % aumento)
print("Valor do aumento: R$ %.2f" % valorAumento)
print("Salario após reajuste: R$ %.2f" % novoSalario)