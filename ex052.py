#Exercicio de Progressão Aritmética
print('=========================')
print('10 TERMOS DE UMA PA')
print('=========================')

termo = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
décimo = termo + (10 - 1) * r
#fórmula do 10 termo da PA

for c in range(termo, décimo+r, r):
    pa = termo +(c-1)* r
    print('{}'.format(c))

print('ACABOU')
