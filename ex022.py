nome = str(input('Digite seu nome completo: ')).strip()
#.strip() elimina espaços antes e depois
primeiro_nome = nome.split()


print("""Analisando seu nome...
Seu nome em maiúsculas é {}
Seu nome em minúsculas é {}
Seu nome tem ao todo {} letras
Seu primeiro nome é {} e ele tem {} letras""".format(nome.upper(),nome.lower(),len(nome)-nome.count(' '),primeiro_nome[0], len(primeiro_nome[0])))