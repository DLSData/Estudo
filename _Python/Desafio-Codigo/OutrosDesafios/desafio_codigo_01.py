# Desafio de codigo Python - 1º #

entrada = input("Dados para calculo de ICM: ").split(" ")

distancia = int(entrada[0])
diametro1 = int(entrada[1])
diametro2 = int(entrada[2])

icm = float(distancia / (diametro1 + diametro2))

#print(f"O ICM para Palantirs de Sauron e Saruman é: {icm:.2f} ")
print(f"{icm:.2f}")