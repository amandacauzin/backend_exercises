import datetime

atual = datetime.date.today().year
totalmaior = 0
totalmenor = 0

for pessoa in range(1, 8):
    ano = int(input('Em que ano a {} pessoa nasceu? '.format(pessoa)))
    idade = atual - ano
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalmaior))
print('E também tivemos {} pessoas menores de idade'.format(totalmenor))
