lista = []
for v in range(0,5):
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    lista = sorted(lista)
    if valor == lista[-1]:
        print(f'Adicionado ao final da lista...')
    else:
        print(f'Adicionado na posição {lista.index(valor)} da lista.')

print('-='*20)
print(f'Os valores digitados em ordem foram {lista}')