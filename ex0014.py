#Aluguel de Carros
dias = float(input('Quantos dias alugados?'))
km = float(input('Quandos Km rodados?'))

t = (60 * dias) + (0.15 * km)

print('O total a pagar é de R${:.2f}'.format(t))