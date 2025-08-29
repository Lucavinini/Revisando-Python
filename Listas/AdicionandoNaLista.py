#Podemos implementar mais um elemento no final da lista por meio do método .append()

#podemos tornar isso ainda mais interativo, criando uma interface interativa.

Cardapio = ["Lasanha", "Bolo de Laranja","Suco de Maracujá" ] # Lista com dados.

cont = 0

while cont < 1: #Loop para exibir a interface e receber uma entrada.

    print("---------Lista de tarefas-----------")
    print("1. Exibir Lista")
    print("2. Inserir tarefa na lista")
    print("3. Sair")
    print("------------------------------------")
    escolha = input()

    if(escolha == "1"):
        print(Cardapio) # printa a lista
    else:
        if(escolha == "2"):
            print("Digite a nova comida:")
            NovaComida = input()
            Cardapio.append(NovaComida) # Uso do novo método.
            print("Nova Comida Adicionada!!")
        else:
            if(escolha == "3"):
                cont += 1
                print("Saindo..")
