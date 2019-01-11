"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
nome = input("Informe seu nome")
while len(nome) < 3:
    print("Nome deve conter ao menos 3 letras")
    nome = input("Informe seu nome")

idade = int(input("Informe sua idade"))
while idade < 0 or idade > 150:
    print("Idade não pode ser negativa nem superior a 150")
    idade = int(input("Informe sua idade"))

salario = float(input("Informe seu salário"))
while salario < 0:
    print("Salário não pode ser negativo")
    salario = float(input("Informe seu salário"))

validosSexo = ['f', 'm']
sexo = input("Informe seu sexo (f ou m)")
while sexo not in validosSexo:
    print("Sexo deve ser f ou m")
    sexo = input("Informe seu sexo (f ou m)")

validosEstadoCivil = ['s', 'c', 'v', 'd']
estadoCivil = input("Informe seu estado civil ('s', 'c', 'v', 'd')")
while estadoCivil not in validosEstadoCivil:
    print("Estado civil inválido")
    estadoCivil = input("Informe seu estado civil ('s', 'c', 'v', 'd')")