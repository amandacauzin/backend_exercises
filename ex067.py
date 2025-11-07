v = soma = 0

while True:
    n= int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    v += 1
    soma += n
print(f'A soma dos {v} valores foi {soma}')