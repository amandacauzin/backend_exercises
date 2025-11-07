from random import randint

print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
vitoria = 0

while True:
    v = int(input('Diga um valor: '))
    op = str(input('Par ou Ímpar? [P/I] ')).upper()
    n = randint(1, 10)
    print(f'Você jogou {v} e o computador {n}.',end='')
    if (v+n) % 2 == 0 and op == 'P':
        print(f'Total de {v+n} DEU PAR')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 15)
    elif (v+n) % 2 != 0 and op == 'I':
        print(f'Total de {v + n} DEU ÍMPAR')
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-'*15)

    else:
        break
    vitoria += 1
print(f'Total de {v + n}')
print('Você PERDEU!')
print('=-'*15)
print(f'GAME OVER! Você venceu {vitoria} vezes.')