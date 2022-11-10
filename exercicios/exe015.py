dias = int(input('Informe o total de dias que foi alugado '))
km = float (input('Quantos quilômetros foram percorriddos por você:'))
valor_final = (60*dias) + (0.15*km)
print ('O valor final a ser pago é {:.2f} R$'.format(valor_final))

