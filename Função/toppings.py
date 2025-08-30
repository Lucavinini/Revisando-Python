#E quando eu não souber a quantidade de parâmetros que vou precisar?

# usando o *toppings, podemos fazer com que o python trabalhe
#com esse parametros.

def pizza(*toppings):
    print(toppings)


pizza('Mussarela', 30, 'Queijo')