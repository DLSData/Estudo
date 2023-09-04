# Conversao de tipos
idade = '26' # tipo str
num1 = 10    # tipo int
num2 = 20    # tipo int

# atribui soma convertendo variavel string para variavel inteira
soma = int(idade)+num2
print(soma)
print("\n")

# sintaxe de Conversao de tipos entre parenteses 
#int()
soma = int(idade)+num2
print(soma, type(idade), type(soma))
print("\n")

#str()
idade_inteira = str(num1)
print(num1, type(num1), type(idade_inteira))
print("\n")

#float()
decimal = float(num2)
print(num2, type(num2), type(decimal))
print("\n")

#bool()
boleano = bool(num1)
print(num1, type(num1), boleano, type(boleano))
print("\n")