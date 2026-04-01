def soma(a, b):
    print(f'A = {a} e B = {b}')
    s= a + b
    print(s)
def contador(* num):
        tam = len(num)
        print(f'Recebi os valores {num} e são ao todo {tam} numeros')

#
#programa principal
soma(4, 5)
soma(8, 9)
contador(2,1,7)
contador(4,4,7,6,2)
