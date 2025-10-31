print('Gerador de PA')
print('-='*10)

a1 = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

n=1

while n < 11:
    t = a1 + ((n-1) * r)
    print('{}'.format(t), end='')
    print(' -> ' if n < 10 else ' -> FIM',end='')
    n += 1