valor_casa = float(input('Digite o valor da casa (R$): '))
salario = float(input('Digite o valor do seu sálario (R$): '))
meses = float(input('Em quantos meses quer pagar a casa? '))

valor_mensal = valor_casa/meses
valor_mensal_possivel = salario*0.30
print('Valor da parcela: {:.2f}R$'.format(valor_mensal))
print('Valor possivel da parcela {:.2f}R$'.format(valor_mensal_possivel))

if valor_mensal_possivel >= valor_mensal:
    print('Você pode comprar a casa!')
else:
    print('Você não pode comprar a casa!')

