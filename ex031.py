d = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(d))

if d<= 200:
    v = d * 0.50
    print('E o preço da sua viagem será de R${:.2f}'.format(v))
else:
    v = d * 0.45
    print('E o preço da sua viagem será de R${:.2f}'.format(v))