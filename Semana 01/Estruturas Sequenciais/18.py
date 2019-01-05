tamanho = float(input("Tamanho de arquivo para download (MB): "))
velocidade = float(input("Velocidade de download (Mbps): "))

tempoSegundos = tamanho / (velocidade * 0.125)
tempoMinutos = tempoSegundos / 60

print(tempoMinutos)