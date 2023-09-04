# Estruturas em lista

# Cria de lista entre colchetes 
lista = []         # lista vazia
lista = list()     # lista vazia
nota = [5]         # lista com numero de posicoes

# Lista permite variaveis de tipos diferentes
nota = [20,'nome', 3.1415, True] # tipos diferentes
nota = [20, 'nome',[10,7,8]]     # lista dentro de lista

# Indexacao e Slices (fatiamento)
print(nota[0])      # indice posicao 1
print(nota[-1])     # ultimo elemento
print(nota[-2])     # penultimo elemento
print(nota[-3])     # antepenultimo elemento
print(nota[2:3:1])  # faixa da lista

# Comprimento da lista
print('Comprimento da lista', len(nota))

# Iteracao de Repeticao FOR com lista
for elemento in lista:
    print (elemento)

for i in nota:
    print(nota[i])

for i in range(len(nota)):
    print(nota[i])


#Métodos

# Append (Adiciona item no final da lista)
lista = [1,5,10,20,21,18]
lista.append(12)

# Insert (Adiciona item na posicao desejada da lista)
lista = [1,5,10,20,21,18]
lista.insert(3,12)

# Extend (Adiciona itens de uma lista no final da lista)
lista = [1,5,10,20,21,18]
lista2 = [19,11,4]
lista.extend(lista2)

# pop (Remove o indice do elemento)
lista.pop()    # remove o ultimo indice
lista.pop(1)   # remove o indice desejado

# remove (Remove o elemento)
lista.remove(3) # remove o elemento (nao o indice)

# count
lista.count(11) # Conta quantos elementos de valor desejado

# index
lista.index(10) # Mostra o indice do elementos desejado

# sort
lista.sort()              # Ordena a lista A-Z
lista.sort(reverse=True)  # Ordena a lista Z-A


# Funcoes

# len
len(lista)    # Mostra tamanho da lista

# sum
sum(lista)    # Soma valores da lista

# max
max(lista)    # Mostra maior valor da lista

# min
min(lista)    # Mostra menor valor da lista









