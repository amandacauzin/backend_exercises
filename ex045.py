print('--------------LOJAS GUANABARA--------------')
p = float(input('Qual o preço da sua compra? R$ '))
print("""FORMA DE PAGAMENTO:
[ 1 ] à vista (dinheiro ou cheque)
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] em 3x ou mais no cartão.""")
o = int(input('Digite sua opção: '))

if o == 1:
    v = p - (p * (10/100))
    print('O valor da sua compra ficou R${:.2f} na opção À VISTA (dinheiro ou cheque)'.format(v))
elif o == 2:
    v = p - (p * (5/100))
    print('O valor da sua compra ficou R${:.2f} na opção À VISTA (cartão)'.format(v))
elif o == 3:
    v = p
    print('O valor da sua compra ficou R${:.2f} na opção 2x (cartão)'.format(v))
elif o == 4:
    v = p + (p * (20/100))
    print('O valor da sua compra ficou R${:.2f} na opção 3x ou mais (cartão)'.format(v))
else:
    print('Você digitou uma opção inválida. Tente novamente.')