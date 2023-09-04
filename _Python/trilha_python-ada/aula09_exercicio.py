"""#Exercicio 1
cont = 0
resultado = 0
n = 10

while cont != n:
    resultado = resultado + 1/(2**cont)
    cont = cont + 1

print(resultado)
"""


"""#Exercicio 2
for _ in range(10):
    print(" 1 Olá, mundo!") 

for _ in "let's code":
    print(" 2 Olá, mundo!")

for _ in " "*10:
    print(" 3 Olá, mundo!")

for _ in range(10, 20, 1):
    print(" 4 Olá, mundo!")

for _ in [10]:
    print(" 5 Olá, mundo!")

for _ in [10]*10:
    print(" 6 Olá, mundo!")"""


"""# Exercicio 3
lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]
lista_final = []

for item in lista_inicial:
    if item % 2 == 0:
        if item < 0:
            lista1 = lista_final.append()
        else:
            lista2 = lista_final.append()
    else:
        if item < 0:
            lista3 = lista_final.append()
        else:
            lista4 = lista_final.append()

print (-2*lista1, 2*lista2, -lista3, lista4 )
print (-lista1, lista2, -2*lista3, 2*lista4 )
print (2*lista1, -2*lista2, lista3, -lista4 )
print (lista1, -lista2, 2*lista3, -2*lista4 )
print (-lista1, 2*lista2, -2*lista3, lista4 )"""


lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]
lista_final = []


for item in lista_inicial:
    if item % 2 == 0:
        if item < 0:
            lista_final.append(-item)
        else:
            lista_final.append(item)
    else:
        if  item < 0:
            lista_final.append(-2*item)
        else:
            lista_final.append(2*item)

print(lista_inicial[:])
print(lista_final[:])
