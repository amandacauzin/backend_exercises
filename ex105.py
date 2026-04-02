def area(l, c):
    area = l * c
    print(f'A área do seu terreno de {l:.2f}m x {c:.2f}m é igual a {area:.2f} m²')

#PROGRAMA PRINCIPAL
print('CONTROLE DE TERRENOS')
print('-'*30)
l = float(input('Digite a largura do terreno: (m)'))
c = float(input('Digite o comprimento do terreno: (m)'))

area(l, c)