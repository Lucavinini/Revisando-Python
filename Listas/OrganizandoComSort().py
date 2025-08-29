#o método sort() organiza a lista em ordem alfabética.

alfabeto = ["c", "A", "i"]
print(alfabeto)

print("Organizando...")
alfabeto.sort()

print(alfabeto)

#Podemos inverter essa ordem usando reverse=True

alfabeto.sort(reverse=True)

print("Invertendo...")
print(alfabeto)

#Lembrando que o sort() altera a lista permanentemente




#Podemos organizar a lista apenas a na exibição, usando o comando sorted()

Letras = ["C", "A", "D"]
print(Letras)

print("Alterando ela na exibição...")
print(sorted(Letras))

print("Mostrando o original...")
print(Letras,"\n")


#Alterando a ordem alfabética com o parametro reverse=true

print(Letras, reverse=True)


#Podemos ainda alterar a ordem usando o reverse()

Letras.reverse()

print(Letras)

Letras.reverse()
print(Letras)



