n = str(input('Digite um número: '))
unidade = n[-1]
dezena = n[-2]
centena = n[-3]
milhar = n[-4]

print("""Analisando o número {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(n, unidade, dezena, centena, milhar ))