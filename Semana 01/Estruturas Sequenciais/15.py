valorHora = float(input("Quanto você ganha por hora: "))
horasTrabalhadas = float(input("Quantas horas você trabalhou: "))

salarioBruto = horasTrabalhadas * valorHora
ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - ir - inss - sindicato

print("Salário Bruto: R$ %.2f" % salarioBruto)
print("IR R$ %.2f" % ir)
print("INSS: R$ %.2f" % inss)
print("Sindicato: R$ %.2f" % sindicato)
print("Salário Líquido: R$ %.2f" % salarioLiquido)