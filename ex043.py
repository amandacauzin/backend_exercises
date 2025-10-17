l1 = int(input('Digite o primeiro segmento: '))
l2 = int(input('Digite o segundo segmento: '))
l3 = int(input('Digite o terceiro segmento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l3:
    if l1 == l2 == l3:
        print('TRIÂNGULO EQUILÁTERO: todos os lados iguais')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('TRIÂNGULO ISÓSCELES: dois lados iguais')
    else:
        print('TRIÂNGULO ESCALENO: todos os lados diferentes.')
else:
    print('Com esses valores digitados NÃO se pode formar um triângulo!')