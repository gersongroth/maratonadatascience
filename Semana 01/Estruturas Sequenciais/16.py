tamanho = float(input("Informe o tamanho a ser pintado (m2): "))

litros = tamanho / 3
latas = litros / 18
galoes = litros / 3.6


nLatas = round(latas)
vLatas = nLatas * 80
vGaloes = round(galoes) * 25

print("Latas:" , nLatas)
print("R$ %.2f" % vLatas)

