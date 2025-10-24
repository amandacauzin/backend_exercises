soma = 0
nomevelho = ''
velho = 0
maioridadehomem = 0
feminino = 0

for pessoas in range(1,5):
    print('----- {}ª pessoa -----'.format(pessoas))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: '))

    soma += idade

    if pessoas == 1 and sexo == "Mm":
        velho = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo == 'Ff' and idade < 20:
        feminino += 1

media = soma/4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(feminino))



