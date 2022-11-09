def converte_real (valor):
	return ('{:.2f} R$'.format(valor)).replace('.', ',')	
	

def aumentar(valor=0, acrescimo=0, formatar=True):
	acrescimo = acrescimo/100
	if (acrescimo  > 100 or acrescimo < 0):
		print ('porcentagem de aumento inválido.')
		return valor	
	else:
		if formatar: 
			return converte_real(valor + (valor*acrescimo))
		else:
			return valor + (valor*acrescimo)
			

def diminuir(valor=0, decrescimo=0, formatar=True):
	decrescimo = decrescimo/100
	if (decrescimo  > 100 or decrescimo < 0):
		print ('porcentagem de aumento inválido.')
		return valor	
	else:
		if formatar: 
			return converte_real(valor + (valor*decrescimo))
		else:
			return valor - (valor*decrescimo)
	

def dobro (valor=0, formatar=True):
	if formatar:
		return converte_real(valor*2)
	else:
		valor*2


def metade (valor=0, formatar=True):
	if formatar:
		return converte_real(valor/2)
	else:
		return valor/2	
