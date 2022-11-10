soma = int(0)
for c in range(0,6):
    n = int(input('Informe um número: '))
    if n %  2 == 0:
        soma = soma + n
print('A soma de todos os números pares foi: {}'.format(soma))        