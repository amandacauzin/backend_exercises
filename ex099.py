cad = list()
dados = dict()
soma = media = 0

while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))

    while True:
        dados['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    cad.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-_'*40)
print(f'Ao todo temos {len(cad)} pessoas cadastradas')
media = soma / len(cad)
print(f'A média de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram: ', end='')

for p in cad:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()

print(f'Lista das pessoas que estão acima da média: ')
for p in cad:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print(f'ENCERRADO!')



