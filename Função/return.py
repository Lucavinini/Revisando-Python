# Pode-se usar o return para retornar um dado ou um conjunto deles.

def Soma(number1,number2):

    resultado = number1+number2

    return resultado # dado que está sendo enviado de volta.


ano1 = 2020
ano2 = 1000

resultado = Soma(ano1, ano2) #Sempre que uma função tem um retorno, a informação que volta precisa ser
                             #armazenada em uma variável para que possamos trabalhar com ela.

print(resultado)