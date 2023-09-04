# Desafio: Criando um sistema bancário

Desafio de código proposto no curso de Python da DIO

## Objetivo Geral
Criar um sistema bancário com operações com funções básicas:
sacar, depositar, visualizar extrato, criar usuario, criar conta e listar contas cadastradas.

## Contexto do Desafio
Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python.
Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.
Na segunda versão do sistema foram adicionadas mais 3 funçoes: criar um novo usuário, criar contas e listar contas existentes.


## Observações
A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. 

A v2 foi aprimorada a estrutura do código e insere novas funções como a criação de novos usuários e novas contas, o sistema não permite o cadastro duplicado de usuários, porém permite o cadastro de várias contas para o mesmo usuário.

## Regras das Funcionalidades

### Validações:
- [x] Saldo suficiente para saque
- [x] Numero de limites de saques diarios
- [x] Saque maior que o permitido
- [x] CPF existente na base de clientes.

### Deposito
- [x] Valores positivos
- [x] Valores armazenados em uma variável
- [x] Exibir os valores em "Extrato"

### Saque
- [x] Valores positivos
- [x] Limite de 3 Saques diários
- [x] Valor máximo permitido por saque : 500.00
- [x] Valores armazenados em uma variável
- [x] Exibir os valores em "Extrato"

### Extrato
- [x] Listar todas as operações efetuadas
- [x] Finalizar extrato com a Exibição do saldo atual 
- [x] Exibir valores em formato moeda (R$)

### Usuários
- [x] Criação de Novo Usuário.
- [x] Cadastro exclusivo para usuário.

### Contas
- [x] Criação de Novas Contas
- [x] Listar todas contas existentes.


