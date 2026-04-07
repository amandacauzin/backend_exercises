def fatorial(n,show=False):
    """
    -> calcula o Fatorial de um número
    :parâmetro n: O número a ser calculado
    :parâmetro show: (opcional) mostra ou não a conta
    :return: O valor de fatorial de um numero N
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#Programa Principal
n = int(input('Digite um numero para descobrir seu fatorial: '))
print(fatorial(n, True))





#EXPLICAÇÃO
#def -> define função
#(f = 1) fatorial igual a 1
#for: para contagem no intervalo de numero até 0, diminuindo
#se tiver show=True
#        print(c, end='') imprimir contagem
#        if c > 1: se a contagem for maior que 1 imprimir o X
#        else: se não imprimir o igual
#    f *= c conta de fatorial: fatorial = contador x numero
#return f imprimir resultado
