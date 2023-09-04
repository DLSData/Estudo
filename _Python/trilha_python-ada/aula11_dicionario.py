# Cria dicionario
livro = {}
livro = dict()

# Estrutura do dicionario
livro = {'titulo':'Code Clean', 'ano':2012, 'valor':12.50}

# Exibe dicionario
print(livro)
print(livro['valor'])

# Adiciona label e valor no dicionario
livro['autor'] = 'Cultura'
print(livro)

# Altera label e valor no dicionario
livro['autor'] = 'Maximo Livro'
print(livro)


# Percorre as chaves do dicionario com FOR
for chave in livro:
    print(chave, livro[chave])

# Busca chave do dicionario com print (retorna true or false)
print('nome'in livro)
print('valor'in livro)

