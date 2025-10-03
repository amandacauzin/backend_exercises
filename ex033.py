p = float(input('Primeiro valor:'))
s = float(input('Segundo valor:'))
t = float(input('Terceiro valor:'))

if p < s and p < t:
    print('O menor valor digitado foi {:.0f}'.format(p))

if s < t and s < p:
    print('O menor valor digitado foi {:.0f}'.format(s))

if t < p and t < s:
    print('O menor valor digitado foi {:.0f}'.format(t))

if p > s and p > t:
    print('O maior valor digitado foi {:.0f}'.format(p))

if s > t and s > p:
    print('O maior valor digitado foi {:.0f}'.format(s))

if t > p and t > s:
    print('O maior valor digitado foi {:.0f}'.format(t))