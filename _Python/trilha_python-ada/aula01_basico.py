#Comando Basico Exibir em tela
print ('Hello World')

#Atribuir uma entrada a uma variavel
nome = input('Qual seu nome: ')
print ('Meu nome é: ' + nome) # concatena string com variavel sem espaco
print ('Meu nome é:' + nome) # concatena string com variavel sem espaco

print ('Meu nome é:', nome)  # concatena string com variavel COM espaco



# Função input(). sempre retorna os valores em string.
# Assim, se os dados esperados do usuário forem numéricos, 
# é importante realizar a conversão dos tipos de dados para que eles possam ser processados.
# Sintaxe = int(input ('o texto: '))
idade = input('Qual sua idade: ')
print(idade, type(idade))

idade = int(input ('Qual sua idade: '))
print(idade, type(idade))