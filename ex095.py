#fazer um programa que leia o nome do aluno e a média dele e diga se esta aprovado, reprovado ou na média. - dentro de um dicionário
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >=7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
        aluno['situação'] = 'RECUPERAÇÃO'
else:
        aluno['situação'] = 'REPROVADO'
print('-='*20)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
