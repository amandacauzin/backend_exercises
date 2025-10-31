print('Gerador de PA')
print('-='*10)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
n = 1
decimo = 11
soma = 0

while n < decimo:
    t = a1 + ((n-1) * r)
    print('{}'.format(t), end='')
    print(' -> ' if n < (decimo-1) else ' -> PAUSA', end='')
    n += 1
    soma += 1
    if n >= decimo:
        nt = int(input('\nQuantos termos você quer mostrar a mais? '))
        decimo = nt + decimo
        if nt == 0:
            print('Progressão finalizada com {} termos mostrados.'.format(soma))

