n1 = int(input('Digite sua primeira nota: '))
n2 = int(input('Digite sua segunda nota: '))

m = (n1 + n2)/2

if m < 5:
    print('REPROVADO. Sua média foi {}.'.format(m))

elif 5 <= m < 7:
    print('RECUPERAÇÃO. Sua média foi {}.'.format(m))

else:
    print('APROVADO. Sua média foi {}.'.format(m))