def ExibirMenu():
    print("------------------------------")
    print("1. Exibir lista")
    print("2. Adicionar na lista")
    print("3. Adicionando na posição")
    print("------------------------------")

Lista = []
cont = 0;

while( cont < 1):

    ExibirMenu()
    op = int(input())

    if(op == 1):
        print(Lista) # Mostrando os valores da lista
    else:
        if(op == 2): #Adicionando na lista pelo .append()
            print("Digite o valor a ser inserido na lista")
            info = input()
            Lista.append(info) 
            print("Novo valor adicionado!")
        else:
            if(op == 3): #Adicionando em posições por meio do insert.()
                print("Digite o valor a ser armazenado")
                info = input()
                print("Digite a posição")
                posi = int(input())
                Lista.insert(posi, info)
                print("Valor adicionado na lista")






