def metrosToCentimetros(metros):
    return metros * 100

tamanhoMetros = float(input("Informe o tamanho (em metros): "))

print("%.0f centímetros" % metrosToCentimetros(tamanhoMetros))