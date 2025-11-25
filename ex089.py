matriz = []
par = terceira = maior = 0

for linha in range (0,3):
    lista = []
    for coluna in range (0,3):
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        lista.append(valor)
        if valor % 2 == 0:
            par += valor
        if coluna == 2:
            terceira += valor
        if linha == 1:
            if coluna == 0:
                maior = valor
            else:
                if valor > maior:
                    maior = valor



    matriz.append(lista)

print('-='*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {terceira}.')
print(f'O maior valor da segunda linha é {maior}')


