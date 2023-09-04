""" Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python. 
O objetivo é implementar três operações essenciais: depósito, saque e extrato. 
O sistema será desenvolvido para um banco que busca monetizar suas operações. 
"""

# iniciando as variaveis

valor = 0.00
saldo = 0.00
saque_limite_dia = 3 
saque_maximo_cada = 500.00
saque_realizado = 0
extrato = ""


# Executando Operacoes conforme Opcoes do MENU

while True:
    menu = int(input("""
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [0] Sair
                    
        >  """))
    
    # Deposito
    if menu == 1:
        valor = float(input("Digite o Valor desejado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: + R$ {valor:.2f}\n"
            print(f'Depósito no valor de R$ {valor:.2f} realizado com sucesso!')
            print(f'Saldo atualizado: {saldo:.2f}')
        else:
            print('Valor inválido! Tente novamente.')
    
    # Saque
    elif menu == 2: 
        valor = float(input("Digite o Valor desejado: "))
        if saque_limite_dia == saque_realizado:
            print('Operaçao nao realizada! Excedido Quantidade de saques diário!')
        elif valor < 0 or valor > saque_maximo_cada:
            print('Operaçao nao realizada! Valor ultrapassa limite de Saque por operação.')    
        elif valor > saldo:
            print('Operaçao nao realizada! Saldo insuficiente.')    
        else:
            saque_realizado += 1
            saldo -= valor
            extrato += f"Saque :   - R$ {valor:.2f}\n"
            print(f'Saque no valor de R$ {valor:.2f} realizado com sucesso!')
            print(f'Saldo atualizado: {saldo:.2f}')
    
    #Extrato
    elif menu == 3:
        if extrato == "":
            print('Não foram realizadas movimentações.')
        else:
            print("========Extrato Bancário=======")
            print(extrato)
            print(f"\nSaldo Final===> R$ {saldo:.2f}")
            print("===============================")
    elif menu == 0:
        print("Sessão finalizada! Obrigado!")
        break
    else:
        print("Operação inválida! Selecione novamente a operação desejada.")