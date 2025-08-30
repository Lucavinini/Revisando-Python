#Podemos ter algumas formas de import.

# import de tudo

#Fazemos: import Nome_do_Modulo

#sempre que fizemos uma chamada de função em alguma parte do código
#que envolva esse módulos:

# resultado = Nome_do_Modulo.NomedaFuncao()

import operacoes

number1 = 24
number2 = 33

minhaSoma = operacoes.Soma(number1,number2)

print(minhaSoma)

#importando alguns métodos:

#from Nome_do_Modulo import NomeDoMetodo, NomeDoMetodo

#from multi import Multi

#MinhaMulti = Multi(2,2)

#print(MinhaMulti)

#Podemos também dar nomes as importações

import multi as op

soma2 = op.Multi(2,2)

print(soma2)