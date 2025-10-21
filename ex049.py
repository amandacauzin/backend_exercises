soma = 0
contagem = 0

for n in range(1, 501, 2):
    if n % 3 == 0:
        soma = soma + n
        contagem = contagem + 1
print('A soma de todos os {} valores solicitados é {}'.format(contagem, soma))