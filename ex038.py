n = int(input('Escreva um número inteiro qualquer: '))
print("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
c = int(input('Escolha sua opção: '))


if c==1:
    print(bin(n)[2:])
elif c==2:
    print(oct(n)[2:])
elif c==3:
    print(hex(n)[2:])
else:
    print('Opção inválida! Tente novamente.')