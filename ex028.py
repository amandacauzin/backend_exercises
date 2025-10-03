import random

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)

n = float(input('Em que número eu pensei? '))
n_escolhido = random.randint(0,5)

print('PROCESSANDO...')

if n==n_escolhido:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {:.0f} e não no número {:.0f}'.format(n_escolhido, n))
