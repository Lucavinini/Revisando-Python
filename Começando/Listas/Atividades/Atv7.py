#Continuando...

Convidados = ["Drácula", "Homem-Aranha", "Jane Austen"]

x = 0

print(Convidados[2] + " Não poderá participar do jantar.")

Convidados.remove("Jane Austen")

Convidados.insert(2, "Shinji Ikari")

print("Encontrei uma mesa maior, vamos chamar mais pessoas!")

Convidados.insert(0, "Anna Beatryz")
Convidados.insert(3, "David Henrique")
Convidados.append("Emily Bronte")


print("Poxa, infelizmente só posso dar espaço para duas pessoas jantarem.")

y = 4

while (len(Convidados) > 2):

    Pessoa_Removida = Convidados.pop()
    print("Me Desculpe "+ Pessoa_Removida + " Fica para a próxima.\n")

print(Convidados[0] + " Você ainda está convidado para jantar comigo!")
print(Convidados[1] + " Você ainda está convidado para jantar comigo!")

del Convidados[1]
del Convidados[0]

print(Convidados)
