#Podemos inserir os elementos na ordem que desejamos por meio do comando .insert(posicao, elemento)

Pecas = ["Rosca", "Cola", "Fusível", "Bateria"]

print(Pecas)
print("Digite o nome do novo item ao almoxarifado")

a = input()

Pecas.insert(0, a)

print(Pecas)

