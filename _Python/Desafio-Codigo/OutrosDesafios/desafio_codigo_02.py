# Calcule a média de cachorros quentes consumidas por participante e imprima o valor com DUAS casas decimais.

valores = input(" dados da competicao ").split(" ") 

hot_dogs_consumidos = int(valores[0])
total_participantes = int(valores[1])
media = float(hot_dogs_consumidos / total_participantes)

print (f"{media:.2f}")