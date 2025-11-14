n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: '))

if num >= 0 and num <=20:
    print(f'Você digitou o numero {n[num]}.')
else:
    for numero in range(num):
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
        if num >= 0 and num <= 20:
            print(f'Você digitou o numero {n[num]}.')
            break

#while True:
#   num = int(input('Digite um numero entre 0 e 20: '))
#   if 0 <= num <= 20:
#       break
#   print('Tente novamente. ',end='')