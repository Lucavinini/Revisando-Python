#Você acabou de descobrir que sua nova
#mesa de jantar não chegará a tempo para o jantar e tem espaço para somente
#dois convidados.
#• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que
#mostre uma mensagem informando que você pode convidar apenas duas
#pessoas para o jantar.
#• Utilize pop() para remover os convidados de sua lista, um de cada vez, até
#que apenas dois nomes permaneçam em sua lista. Sempre que remover um
#nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela
#saiba que você sente muito por não poder convidá-la para o jantar.
#• Apresente uma mensagem para cada uma das duas pessoas que continuam
#na lista, permitindo que elas saibam que ainda estão convidadas.
#• Utilize del para remover os dois últimos nomes de sua lista, de modo que você
#tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem
#uma lista vazia no final de seu programa.

x = 0
y = 5

Convidados = ["Drácula", "Homem-Aranha", "Jane Austen"]

print(Convidados[2] + " Não poderá participar do jantar.")

Convidados.remove("Jane Austen")

Convidados.insert(2, "Shinji Ikari")

print("Oi "+ Convidados[0] + " venha jantar comigo!")
print("Olá "+ Convidados[1] + " venha jantar comigo e com o " + Convidados[0])
print("Olá "+ Convidados[2] + " O que acha de jantar comigo e com eles: " + Convidados[1] +" e "+ Convidados[0])

#Nova parte
print("Encontrei uma mesa maior, vamos chamar mais pessoas!")

Convidados.insert(0, "Anna Beatryz")
Convidados.insert(3, "David Henrique")
Convidados.append("Emily Bronte")

while (x <= y):

    print("Olá, bem vindo ao meu jantar " + Convidados[x])
    x += 1









