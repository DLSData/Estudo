""" 
Neste desafio, você terá a oportunidade de otimizar o Sistema Bancário 
previamente desenvolvido com o uso de funções Python. 

O objetivo é aprimorar a estrutura e a eficiência do sistema, 
implementando as operações de depósito, saque e extrato em funções específicas. 

Você terá a chance de refatorar o código existente, 
dividindo-o em funções reutilizáveis, facilitando a manutenção 
e o entendimento do sistema como um todo. 

Prepare-se para aplicar conceitos avançados de programação 
e demonstrar sua habilidade em criar soluções mais elegantes e eficientes utilizando Python. 
"""

# Definindo as Funções

# Menu
def opcoes_menu():
    opcao = int(input("""
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Novo Usuário
        [5] Abertura de Nova Conta
        [6] Lista de Contas
        [0] Sair
                    
        >  """))
    return opcao

# Depósito
def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: - R$ {valor:.2f}")
        print(f'Depósito no valor de R$ {valor:.2f} realizado com sucesso!')
        print(f'Saldo atualizado: {saldo:.2f}')
    else:
        print('Valor inválido! Tente novamente.')
    
    return saldo,extrato
    
# Saque
def saque(*, saldo, valor, extrato, SAQUE_LIMITE_DIA, saque_realizado, SAQUE_MAXIMO_CADA):
    saque_excedido = saque_realizado >= SAQUE_LIMITE_DIA
    limite_excedido = valor < 0 or valor > SAQUE_MAXIMO_CADA 
    saldo_insuficiente = valor > saldo
    
    if saque_excedido:
        print('Operaçao nao realizada! Excedido Quantidade de saques diário!')
    
    elif limite_excedido:
        print('Operaçao nao realizada! Verifique valor da operação.')    
    
    elif saldo_insuficiente:
        print('Operaçao nao realizada! Saldo insuficiente.')    
    
    else:
        saldo -= valor
        saque_realizado += 1
        extrato.append(f"Saque :   + R$ {valor:.2f}")
        print(f'Saque no valor de R$ {valor:.2f} realizado com sucesso!')
        print(f'Saldo atualizado: {saldo:.2f}')
        print(saque_realizado)
        print(SAQUE_LIMITE_DIA)
    return saldo, extrato, saque_realizado

# Extrato
def extrato_saldo(saldo, /, *, extrato):
    if extrato == []:
        print('Não foram realizadas movimentações.')
    else:
        print("========Extrato Bancário=======")
        for operacao in extrato:
            print(operacao)
        print(f"\nSaldo Final===> R$ {saldo:.2f}")
        print("===============================")
    
# Cria Usuario
def cria_usuario(usuarios):
    cpf = input('Informe o CPF do Novo Correntista: (somente números) : ')
    valida_cpf = verifica_cpf(cpf, usuarios)
        
    if valida_cpf:
        print('Cadastro já existente, Verifique operacao!')
        return

    nome = input('Nome Completo: ')
    data_nascimento = input('Data de Nascimento: ')
    endereco = input('Endereço: ')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    uf = input('UF :')
    
    usuarios.append ({
        "cpf":cpf, 
        "nome":nome, 
        "data_nascimento:":data_nascimento, 
        "endereco":endereco, 
        "bairro":bairro, 
        "cidade":cidade, 
        "uf":uf
        })

    print (f'Cadastro de {nome} efetuado com sucesso!')
      
# Verifica CPF    
def verifica_cpf(cpf, usuarios):
        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                return True

# Cria Conta
def cria_conta(usuarios, contas, AGENCIA, numero_conta):
    cpf = input('CPF do usuario: ')
    valida_cpf = verifica_cpf(cpf,usuarios)
    if valida_cpf:
        conta = {'agencia':AGENCIA, 'numero_conta':numero_conta, 'usuario':cpf}
        contas.append(conta)
        
        print (f'''
               Conta corrente para {cpf}, criada com sucesso! 
               Parabéns! 
               Sua conta é : 
               Agência : {AGENCIA}, 
               C/C nº : 000{numero_conta}.''')
    else:
        print ('Cliente não cadastrado!')

# Lista Contas
def lista_contas(contas):
    print ('='*15 + 'Contas cadastradas' + '='*15) # Divisao Pagina

    for conta in contas:
        registro = (f"""\
              Agência : {conta['agencia']}
              C/C : 000{conta['numero_conta']}
              CPF Titular : {conta['usuario']}
              """)
        print (registro)
        print ('-'*50) # Divisao Registro
    
    print ('='*15 + ' Fim do relatório ' + '='*15) # Divisao Pagina

def main ():
    SAQUE_LIMITE_DIA = 3
    SAQUE_MAXIMO_CADA = 500.00
    AGENCIA = '0001'

    valor = 0.00
    saldo = 0.00
    saque_realizado = 0

    extrato = []
    usuarios = []
    contas = []
    

    while True:
        menu = opcoes_menu()

        if menu == 1: # Depositar
            valor = float(input("Digite o Valor desejado: "))
            saldo, extrato = deposito (saldo, valor, extrato)
        elif menu == 2: # Sacar
            valor = float(input("Digite o Valor desejado: "))
            saldo, extrato, saque_realizado = saque( saldo=saldo, valor=valor, extrato=extrato, SAQUE_LIMITE_DIA=SAQUE_LIMITE_DIA, saque_realizado=saque_realizado, SAQUE_MAXIMO_CADA=SAQUE_MAXIMO_CADA)
        elif menu == 3: # Extrato
            extrato_saldo(saldo, extrato=extrato )
        elif menu == 4: # Cadastra Usuário
            cria_usuario(usuarios)
        elif menu == 5: # Abertura conta corrente
            numero_conta = len(contas) + 1    
            cria_conta(usuarios, contas, AGENCIA, numero_conta)
        elif menu == 6: # Lista de contas cadastradas
            lista_contas(contas)
        elif menu == 0: # Encerra sistema
            print("Sessão finalizada! Obrigado!")
            break
        else:
            print("Operação inválida! Selecione novamente a operação desejada.")


main()