total = []
aluno = []

while True:
    nome = str(input('Nome: '))
    aluno.append(nome)
    nota1 = float(input('Nota 1: '))
    aluno.append(nota1)
    nota2 = float(input('Nota 2: '))
    aluno.append(nota2)

    media = (nota1 + nota2) / 2
    aluno.append(media)

    total.append(aluno[:])
    aluno.clear()

    op = str(input('Quer continuar? [S/N]'))
    if op in 'nN':
        break
print('-='*30)
print(f'No.'.ljust(4),end='')
print(f'NOME'.ljust(10),end='')
print(f'MÉDIA'.ljust(6))
print('-'*25)
for i, v in enumerate(total):
    print(f'{i}'.ljust(4),end='')
    print(f'{total[i][0]}'.ljust(10),end='')
    print(f'{total[i][3]}'.ljust(6))
print('-'*25)

while True:
    pos = int(input('Mostrar as notas de qual aluno? (999 interrompe): '))
    if pos == 999:
        print('Finalizando...')
        break
    if pos >= len(total):
        print('Aluno inexistente.')
    else:
        aluno = total[pos]
        print(f'Notas de {aluno[0]} são {aluno[1]} e {aluno[2]}.')
