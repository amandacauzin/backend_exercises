n = int(input('Digite um número: '))
c = str(input('Quer continuar? [S/N]')).upper()
cont = 1
soma = 0
quant = maior = menor = 0

while c != 'N':
    if c == 'S':
        soma = soma + n
        cont += 1
        quant += 1
        if quant == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        n = int(input('Digite um número: '))
        c = str(input('Quer continuar? [S/N]')).upper()
    else:
        print('Esta opção NÃO existe.\nDigite S para sim e N para não.')
        c = str(input('Quer continuar? ')).upper()
#caso seja N:
soma = soma + n
media = soma / cont
print('Você digitou {} números e a média foi {:.2f}.'.format(cont, media))
print('O maior valor foi {} e o menor valor foi {}.'.format(maior, menor))

