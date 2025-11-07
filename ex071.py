print('-'*30)
print('      LOJA SUPER BARATÃO')
print('-'*30)

soma = caro = barato = 0
inicio = 1000000

while True:
    prod = str(input('Nome do Produto: '))
    p = float(input('Preço: R$'))
    op = str(input('Quer continuar? [S/N] ')).upper()

    soma += p
    if p > 1000:
        caro += 1
    if p < inicio:
        inicio = p
        barato = p
        prodbarato = prod


    if op == 'N':
        break

print('---------- FIM DO PROGRAMA ----------')
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {caro} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {prodbarato} que custa R${barato:.2f}')