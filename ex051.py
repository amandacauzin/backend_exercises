soma = 0

for c in range(0,7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
print('A soma dos números pares é igual a {}'.format(soma))