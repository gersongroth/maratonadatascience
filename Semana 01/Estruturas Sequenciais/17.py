tamanho = float(input("Informe o tamanho a ser pintado (m2): "))

litros = tamanho / 6
latas = litros / 18
galoes = litros / 3.6

vLatas = round(latas) * 80
vGaloes = round(galoes) * 25

print("Latas: R$ %.2f" % vLatas)
print("Galões: R$ %.2f" % vGaloes)

