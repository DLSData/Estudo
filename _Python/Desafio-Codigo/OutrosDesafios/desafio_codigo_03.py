# Calcule quantidade de litros necessária para realizar a viagem e imprima com TRÊS dígitos após o ponto decimal

valores = input("dados da viagem").split(" ")

horas_viagem = int(valores[0])
velocidade_km = int(valores[1])
CONSUMO_CARRO_KM = 12

combustivel =  float((velocidade_km * horas_viagem)/CONSUMO_CARRO_KM)

print(f"{combustivel:.3f}")