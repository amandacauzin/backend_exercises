lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        print(f'Valor adicionado com sucesso...')
        lista.append(valor)
    op = str(input('Quer continuar? [S/N]'))
    if op in 'Nn':
        break
print('-='*20)
lista = sorted(lista)
print(f'Você digitou os valores {lista}')