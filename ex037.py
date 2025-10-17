casa = float(input('Qual o valor da casa?: R$'))
s = float(input('Qual o seu salário?: R$'))
anos = float(input('Em quantos anos você pagará a casa?: '))

meses = 12 * anos
prest = casa / meses
men = (30/100) * s

if prest <= men:
    print('Para pagar uma casa de R${:.2f} em {:.0f} anos, a prestação será de {}!'.format(casa, anos, prest))
    print('Seu empréstimo pode ser CONCEDIDO!')
else:
    print('Para pagar uma casa de R${:.2f} em {:.0f} anos, a prestação será de {}!'.format(casa, anos, prest))
    print('Seu emprestimo foi NEGADO')