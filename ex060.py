import time


n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = int(input("""    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
>>>>>Qual é a sua opção? """))
while op != 5 :
    if op == 1:
        s = n1 + n2
        print('A soma entre {} + {} é {}.'.format(n1, n2, s))
    elif op == 2:
        m = n1 * n2
        print('A multiplicação entre {} * {} é {}.'.format(n1, n2, m))
    elif op == 3:
        if n1 > n2:
            print('O maior número é {}'.format(n1))
        elif n1 == n2:
            print('Os números são iguais')
        else:
            print('O maior número é {}'.format(n2))
    elif op == 4:
        n1 = int(input('Digite um novo primeiro número:'))
        n2 = int(input('Digite um novo segundo número:'))
    elif op != 1 and op != 2 and op != 3 and op != 4 and op !=5:
        print('Opção inválida. Tente novamente.')
    time.sleep(2)
    op = int(input("""=-=-=-=-=-=-=-=-=-=-=-=-=
        [ 1 ] somar
        [ 2 ] multiplicar
        [ 3 ] maior
        [ 4 ] novos números
        [ 5 ] sair do programa
    >>>>>Qual é a sua opção? """))

time.sleep(2)
print("""Finalizando...
=-=-=-=-=-=-=-=-=-=-=-=-=
Fim do programa! Volte sempre!""")