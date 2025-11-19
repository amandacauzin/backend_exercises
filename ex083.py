lista = []

while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    op = str(input('Quer continuar? [S/N]'))
    while op not in "SsNn":
        print("ERRO! ESSA OPÇÃO NÃO EXISTE")
        op = str(input('Quer continuar? [S/N]'))
    if op in "Nn":
        break

print('-='*20)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente foram {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')