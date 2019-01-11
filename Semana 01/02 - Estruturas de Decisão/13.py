"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

diaSemana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']
dia = int(input("Informe o dia da semana (1 a 7): "))

if dia < 1 or dia > 7:
    print("Valor inválido")
else:
    print (diaSemana[dia-1])