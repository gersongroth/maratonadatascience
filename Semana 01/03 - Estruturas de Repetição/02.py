"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

def getUser():
    user=input("Informe o nome de usuário: ")
    password= input("Informe a senha: ")

    return user,password

user,password=getUser()
while(user == password):
    print("Senha não pode ser igual ao usuário")
    user,password=getUser()