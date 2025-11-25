lista = []
pares = []
impares = []

for n in range (0,7):
    numero = (int(input(f'Digite o {n+1}º valor: ')))
    lista.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print('-='*30)
pares.sort()
impares.sort()
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores impares digitados foram: {impares}')