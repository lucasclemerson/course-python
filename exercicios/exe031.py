distancia = int(100)
valor = float(0.5 * distancia)

if distancia >= 200:
	valor = 0.45 * distancia

print ('O valor a ser pago pela distância é de {:.2f} R$'.format(valor))
