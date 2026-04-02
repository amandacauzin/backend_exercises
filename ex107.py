from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i:.0f} até {f:.0f} de {p:.0f} em {p:.0f}')
    if i < f:
        cont = i
        while cont <= f:
            print(f' {cont:.0f} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f' {cont:.0f} ' , end='', flush=True)
            sleep(0.5)
            cont -= p
        print('FIM!')

def esp():
    print('-='*20)

#PROGRAMA PRINCIPAL
esp()
contador(1, 10, 1)
esp()
contador(10, 1, 2)
esp()
print('Agora é sua vez de personalizar a contagem!')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
esp()
contador(i,f,p)
