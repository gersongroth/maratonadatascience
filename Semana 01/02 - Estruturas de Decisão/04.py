letra = input("Informe uma letra: ")
vogais = ['a','e','i','o','u']

if len(letra) > 1:
    print("Apenas uma letra é permitida")
elif letra in vogais:
    print("Vogal")
else: # TODO - validar se é consoante
    print("Consoante")