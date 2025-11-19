lista = []
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    op = str(input('Quer continuar? [S/N]'))
    while op not in "SsNn":
        print('ERRO!TENTE NOVAMENTE')
        op = str(input('Quer continuar? [S/N]'))
    if op in 'Nn':
        break
print('-='*20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {sorted(pares)}')
print(f'A lista de ímpares é {sorted(impares)}')