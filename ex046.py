from random import randint

print("""Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA""")
o = int(input('Digite a opção escolhida: '))

aleat = randint(1, 3)

print("""JO
KEN
PÔ!!!""")
print('-=-=-=-=-=-=-=-=-=-=-=')

if o == 1 and aleat == 3:
    print("""Computador jogou tesoura.
    Jogador jogou pedra.""")
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print('JOGADOR VENCE')

elif o == 1 and aleat == 2:
    print("""Computador jogou papel.
    Jogador jogou pedra.""")
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print('COMPUTADOR VENCE')

elif o == 1 and aleat == 1:
    print("""Computador jogou pedra.
    Jogador jogou pedra.""")
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print('EMPATE')

elif o == 2 and aleat == 1:
    print("""Computador jogou pedra.
    Jogador jogou papel.""")
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print('JOGADOR VENCE')

elif o == 2 and aleat == 3:
    print("""Computador jogou tesoura.
    Jogador jogou papel.""")
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print('COMPUTADOR VENCE')

elif o == 2 and aleat == 2:
    print("""Computador jogou papel.
    Jogador jogou papel.""")
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print('EMPATE')

elif o == 3 and aleat == 1:
    print("""Computador jogou pedra.
    Jogador jogou tesoura.""")
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print('COMPUTADOR VENCE')

elif o == 3 and aleat == 2:
    print("""Computador jogou papel.
    Jogador jogou tesoura.""")
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print('JOGADOR VENCE')

elif o == 3 and aleat == 3:
    print("""
    Computador jogou tesoura.
    Jogador jogou tesoura.""")
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print('EMPATE')

else:
    print('Jogada INVÁLIDA')

