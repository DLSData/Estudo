# Estrutura condicional While (nao controlado)

numero_sorteado = 15
numero_escolhido = int(input("Acerte o numero:"))

while numero_escolhido != numero_sorteado:
      numero_escolhido = int(input("Tente novamente:"))

print("Parabens! Voce acertou!")
print("\n")



# Estrutura condicional While (controlado)
contador = 0
numero_sorteado = 15
numero_escolhido = int(input("Tente outro numero:"))

while numero_escolhido != numero_sorteado and contador <4:
    numero_escolhido = int(input("Tente outro numero:"))
    contador = contador + 1
        

if numero_escolhido == numero_sorteado:
    print("Parabens! Voce acertou!")
    print("\n")
else:
    print("Tentativas esgotadas!")
    print("\n")

