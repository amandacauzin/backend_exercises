def ficha(nome='<desconhecido>', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')

#Programa Principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

#se o g é numerico, ele recebe como numero, se não ele recebe 0
#se n(nome) tirar os espaços sobrando e ficar vazio o nome, a função ficha imprime gol= # g
#se não a ficha imprime n e g no lugar de nome e gol