def ExibirMenu():
    print("------------------------------")
    print("1. Exibir lista")
    print("2. Adicionar na lista")
    print("3. Adicionando na posição")
    print("4. Mudando elemento")
    print("5. Descobrindo o tamanho")
    print("6. Remover")
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
            else:
                if(op == 4): # Mudando um valor por meio da posição dele
                    print("Insira a posição que você quer mudar")
                    op = int(input())
                    print("Digite o novo valor")
                    novainfo = input() # Caso a posição não exista, vai dar erro e o código encerra
                    Lista[op] = novainfo
                    print("Valor atualizado!")
                else:
                    if(op == 5): # Tamanho da minha lista usando o len()
                        print("O tamanho da lista é" , len(Lista))
                    else:
                        if(op == 6): #Removendo com o del
                            print("Digite a posição que quer remover")
                            op = int(input())
                            del Lista[op]






