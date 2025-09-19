l = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))

a = l*h
tinta = 1 * (1/2*a)

print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².'.format(l, h, a))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(tinta))
