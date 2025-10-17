from datetime import date

ano = int(input('Digite o ano que você nasceu:'))

idade = date.today().year - ano

if idade == 18:
    print('É hora de se alistar.')
elif idade < 18:
    print('Ainda não é a hora de se alistar.')

    tempo = 18 - idade
    print('Falta(m) {} ano(s) para o alistamento.'.format(tempo))

else:
    print('Já passou da hora de se alistar.')
    tempo = 18 - idade
    print('Você está {} ano(s) atrasado para o alistamento.'.format(tempo))