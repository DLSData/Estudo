# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;
# while True significa que, enquanto houver entradas, o código após o try continuará sendo executado

#status = 0
    
#while status <4:
#    try:
#        perna = str(input("Digite: "))
#        print (perna)
#        if perna == "esquerda":
#            print("ingles")
#        if perna == "direita":
#            print("frances")
#        if perna == "nenhuma":
#            print("portugues")
#        if perna == "ambas":
#            print("caiu")
#        print (status)
#        status += 1
#    except EOFError: 
#        print("Entrada invalida")
#        break
#    print (status)




while True:
    try:
        perna = str(input())
        if perna == "esquerda":
            print("ingles")
        if perna == "direita":
            print("frances")
        if perna == "nenhuma":
            print("portugues")
        if perna == "ambas":
            print("caiu")
    except EOFError: 
        print("Entrada invalida")
        break
    