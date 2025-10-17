p = float(input('Qual é o seu peso?(kg) '))
h = float(input('Qual é a sua altura?(m) '))

imc = p / (h * h)

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('SOBRE PESO')
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA')