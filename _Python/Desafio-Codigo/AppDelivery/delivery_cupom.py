def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
           
   #TODO: Criar as condições para aplicar o cupom de desconto (10% ou 20%).
    cupom_desconto = (input())
    #cupom_desconto = float(input())/100
    if cupom_desconto == '20%':
        total -= total * 0.20
    elif cupom_desconto == '10%':
        total -= total * 0.10
    else:
        print('Cupom invalido')
    #cupom_desconto = (input())
    
    print (f'Valor Total: {total:.2f}')
 
 
if __name__ == "__main__":
    main()