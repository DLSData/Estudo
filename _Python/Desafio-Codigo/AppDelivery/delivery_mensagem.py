#TODO: Imprimir a saida no padrao definido no enunciado deste desafio.
#Dica: Para simplificar a formatacao, utilize o conceito de interpolacao de strings.

def opcaoRestaurante (menu):
    match menu:
      case 1:
        return 'McDonalds', 10
      case 2:
        return 'KFC', 25
      case 3:
        return 'Burger King', 5
      case default:
        return "Opcao Invalida. Tente novamente"

def main():
    menu = int(input(f'''Escolha um Restaurante: 
        1 - McDonalds
        2 - KFC
        3 - Burger King
        >_  '''))
    
    nomeRestaurante, tempoEstimadoEntrega = opcaoRestaurante(menu)

    print ((f"O restaurante {nomeRestaurante} entrega em {tempoEstimadoEntrega} minutos."))

main()

