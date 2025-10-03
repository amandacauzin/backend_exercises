print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)

p = float(input('Primeiro segmento: '))
s = float(input('Segundo segmento: '))
t = float(input('Terceiro segmento: '))

if p < s + t and s < p + t and t < p + s:
    print('Os segmentos acima PODEM FORMAR um triângulo!')

else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')