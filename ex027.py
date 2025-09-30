nome = input('Digite seu nome: ').strip()
nome_completo = nome.split()

print("""Muito prazer em te conhecer!
Seu primeiro nome é {}
Seu último nome é {}""".format(nome_completo[0],nome_completo[-1]))
