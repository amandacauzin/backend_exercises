def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade<16:
        return f'Você tem {idade} anos! VOTO NEGADO.'
    elif idade >= 16 and idade < 18 or idade>65:
        return f'Você tem {idade} anos! Voto Opcional'
    else:
        return f'Você tem {idade} anos! Voto obrigatório!'


#principal
print('-'*40)
print('ELEIÇÕES')
print('-'*40)

ano = int(input('Digite o ano que você nasceu: '))
print(voto(ano))

