
Cardapio = ["Lasanha", "Bolo de Laranja","Suco de Maracujá" ]

print(Cardapio)

#Podemos implementar mais um elemento no final da lista por meio do método .append()

Cardapio.append("Pizza")

print(Cardapio)

#podemos tornar isso ainda mais interativo

print("Você é um chefe de cozinha e deseja adicionar no cardápio do restaurante um pedido, Digite o nome do prato:")

a = input()

Cardapio.append(a)

print(Cardapio)
