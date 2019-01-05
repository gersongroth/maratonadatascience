peso = float(input("Informe o peso: "))

excesso = peso - 50
multa = excesso * 4.0

print("Excesso de peso: %.1f quilos" % excesso)
print("Multa: R$ %.2f" % multa)