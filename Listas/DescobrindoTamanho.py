#A função len() é importante para definir o tamanho de uma lista, com essa informação podemos trabalhar de diversas formas.

ListaNomesMulheres = ["Ana", "Deborah", "Francisca"]

print(len(ListaNomesMulheres))


#Vamos criar uma lista de nomes de mulheres que será avaliada, caso a quantidade de nomes seja inferior a 5, o programa vai sinalizar um erro.

Lista = ["Ana", "Maria", "Lady", "Lindomar", "Elza"] #Mudando essa lista manualmente, podemos ter diferentes fluxos.

if(len(Lista) < 5):
    print("Error")

else:
    print("Válido")