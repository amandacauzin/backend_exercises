#valores de uma matriz 3x3
matriz = []

for linha in range(0,3):
    lista = []
    for coluna in range(0,3):
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        lista.append(valor)
    matriz.append(lista)

print('-=' * 30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[ {matriz[linha][coluna]:^5} ]', end='')
    print()

