def escreva(txt):
    print('~'*(len(txt)+6))
    print(f'   {txt}   ')
    print('~'*(len(txt)+6))

while True:
    txt = str(input('Digite um texto: (digite PARAR para interromper o programa)'))
    if txt == 'parar':
        print('Programa Encerrado!')
        break
    escreva(txt)
