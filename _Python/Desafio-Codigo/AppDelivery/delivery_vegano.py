numPedidos = int(input())
    
for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input()
    if ehVegano == 's':
      print(f'Pedido {i}: {prato} (Vegano) - {calorias} calorias')
    else:
      print(f'Pedido {i}: {prato} (Nao-vegano) - {calorias} calorias')
    
#TODO: Tendo em vista a variável booleana "ehVegano", imprima a saída deste desafio.
