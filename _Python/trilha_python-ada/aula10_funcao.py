

# Cria Funcoes
def mensagem():
    print('bom dia!')
    print('Iniciamos o dia')
    print('\n')

def mensagem_personal(nome):
    print(f'bom dia, {nome}!')
    print('Iniciamos o dia')
    print('\n')

def mensagem_padrao(nome1='linda'):
    print('bom dia!')
    print(f'{nome1}, Iniciamos o dia')
    print('\n')

# Cria funcao com retorno
def soma (num1, num2):
    return num1+num2
    

# Chama a funcao criada com variavel
nome = 'Rita'
mensagem_personal(nome)

# Chama a funcao criada com constante
mensagem_personal('Denise')

# Chama a funcao criada com default
mensagem_padrao("lindeza")

# Atribui resultado de funcao a uma variavel
resultado = soma(10, 3)
print(resultado)