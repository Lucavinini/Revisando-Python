# Chama-se Tupla, uma lista, cuja os valores não podem ser mudados

raio = (200, 300) #Parenteses definem uma tupla!

print(raio)

#Na printagem usa-se o [] para indicar a posição que queremos printar

print(raio[0])

# Utilizando um for para iterar sobre a tupla
for raios in raio:
    print(raios)

# A única forma de alterar uma tupla é subescrevendo os seus valores

raio = (500, 530)

print(raio)