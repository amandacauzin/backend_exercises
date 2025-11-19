from turtledemo.sorting_animate import instructions1

lista = []
for v in range(0,5):
    valor = (int(input(f'Digite um valor para a posição {v}: ')))
    lista.append(valor)

print('=-'*20)

print(f'Você digitou os valores {lista}')

print(f'O maior valor digitado foi {max(lista)}',end=' ')
print(f'nas posições ',end=' ')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end=' ')
print()

print(f'O menor valor digitado foi {min(lista)}',end=' ')
print(f'nas posições ',end=' ')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end=' ')
print()