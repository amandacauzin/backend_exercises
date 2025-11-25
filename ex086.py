lista = []
principal = []

pessoa = maior = menor = 0
while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista [1] < menor:
            menor = lista[1]

    principal.append(lista[:])
    lista.clear()

    op = str(input('Quer continuar? [S/N]'))
    pessoa += 1
    if op in 'Nn':
        break


print('-='*30)
print(f'Ao todo, você cadastrou {pessoa} pessoas.')
print(f'O maior peso foi de {maior}Kg.', end='')
for p in principal:
    if p[1] == maior:
        print(f' Peso de [{p[0]}]')

print(f'O menor peso foi de {menor}Kg.', end='')
for p in principal:
    if p[1] == menor:
        print(f' Peso de [{p[0]}]')