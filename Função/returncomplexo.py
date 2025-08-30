#É possível retornar estruturas de dados.

def pessoa(nome,idade,altura):

    dicionario = {'nome': nome, 'idade': idade, 'altura': altura}

    return dicionario


Ana = pessoa('Ana', 25, 1.74)

print(Ana)