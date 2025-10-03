s = float(input('Qual é o salário do funcionário? R$'))

if s <= 1250:
    aumento = s + (s * (15 / 100))
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(s, aumento))

else:
    aumento = s + (s * (10 / 100))
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(s, aumento))
