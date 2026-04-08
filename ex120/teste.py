from ex120 import moeda

p = float(input('Digite o preço: R$'))
t = float(input('Digite a taxa: %'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'Aumentando {t:.0f}% temos {(moeda.aumentar(p, t,True))}')
print(f'Diminuindo {t:.0f}% temos {(moeda.diminuir(p, t,True))}')