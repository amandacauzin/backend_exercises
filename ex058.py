s = str(input('Informe seu sexo: [M/F] ')).upper()

while s != 'M' and s != 'F':
    s = str(input('Dados Inválidos. Por favor, informe seu sexo: [M/F} ')).upper()
    if s == 'M' or s == 'F':
        print('Sexo {} registrado com sucesso.'.format(s))