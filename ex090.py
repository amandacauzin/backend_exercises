import random
from time import sleep

print('-'*40)
print(f'JOGA NA MEGA SENA'.center(40))
print('-'*40)
jogo = []

quantidade = int(input('Quantos jogos você quer que eu sorteie? '))

for j in range(0,quantidade):
    numeros_sorteados = random.sample(range(1,61),6)
    numeros_sorteados.sort()
    jogo.append(numeros_sorteados)
    print(f'Jogo {j+1}: {jogo}')
    sleep(1)
    jogo.clear()
print(f'-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')