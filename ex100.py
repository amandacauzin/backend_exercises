time = list()
jogador = dict()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for n in range(0, jogador['partidas']):
        jogador['gols'] = int(input(f'Quantos gols na partida {n+1}? '))
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ESCOLHA S OU N.')
    if resp == 'N':
        break
print(time)
print('-='*35)
print()