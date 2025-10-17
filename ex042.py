from datetime import date

ano = int(input('Digite o ano do seu nascimento: '))

idade = date.today().year - ano

if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <= 19:
    print('CATEGORIA JUNIOR')
elif idade <= 25:
    print('CATEGORIA SENIOR')
else:
    print('CATEGORIA MASTER')