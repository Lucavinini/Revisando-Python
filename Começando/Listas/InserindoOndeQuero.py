#Podemos inserir os elementos na ordem que desejamos por meio do comando .insert(posicao, elemento)

Pecas = ["Rosca", "Cola", "Fusível", "Bateria"]

print(Pecas)

print("Digite o nome do novo item ao almoxarifado")
a = input()

Pecas.insert(0, a) # É importante lembrar que sempre que um item é adicionado na posição já ocupada da lista, 
                   #os elementos seguem nas posições da direita da lista >>


print(Pecas)

