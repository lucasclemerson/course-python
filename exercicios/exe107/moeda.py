def aumentar(valor=0, acrescimo=0):
	acrescimo = acrescimo/100
	if (acrescimo  > 100 or acrescimo < 0):
		print ('porcentagem de aumento inválido.')
		return valor	
	else:
		return valor + (valor*acrescimo)


def diminuir(valor=0, decrescimo=0):
	decrescimo = decrescimo/100
	if (decrescimo  > 100 or decrescimo < 0):
		print ('porcentagem de aumento inválido.')
		return valor	
	else:
		return valor - (valor*decrescimo)


def dobro (valor=0):
	return valor*2


def metade (valor=0):
	return valor/2
