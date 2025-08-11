#Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que
#Você gostaria de visitar;

#armazene as localidades em uma lista. Certifique-se de que a lista não esteja
#em ordem alfabética.

Lugares = ["Tokyo", "Paris", "Inglaterra", "China", "New York"]

#Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma
#elegante; basta exibi-la como uma lista Python pura.

print(Lugares)

#Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a
#lista propriamente dita.

print(sorted(Lugares))

#Mostre que sua lista manteve sua ordem original exibindo-a.

print(Lugares)

#Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar
#a ordem da lista original.

print(sorted(Lugares,reverse=True))

#Mostre que sua lista manteve sua ordem original exibindo-a novamente.

print(Lugares)


#Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar
#que sua ordem mudou.

Lugares.reverse()

#Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista
#para mostrar que ela voltou à sua ordem original.

Lugares.reverse()

#Utilize sort() para mudar sua lista de modo que ela seja armazenada em
#ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.

Lugares.sort()

print(Lugares)

#Utilize sort() para mudar sua lista de modo que ela seja armazenada em
#ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.

Lugares.sort(reverse=True)
print(Lugares)

