from random import randint

print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

t = 1
p = int(input('Qual é o seu palpite? '))
n = randint(0, 11)

while p != n:
    if p < n:
        print('Mais... Tente mais uma vez.')
    elif p > n:
        print('Menos... Tente mais uma vez.')
    p = int(input('Qual é o seu palpite? '))
    t += 1

print('Acertou com {} tentativas'.format(t))