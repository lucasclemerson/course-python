def converte_real (valor):
	return ('R${:.2f}'.format(valor)).replace('.', ',')	
	

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
			return converte_real(valor - (valor*decrescimo))
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
		
		


#mostrar informações atraves do preço fornecido
def resumo (valor=0, aumento=0, reducao=0):
	print ()
	print ('-'*40)
	print ('{:^40}'.format('RESUMO DO VALOR'))
	print ('-'*40)
	
	#preço sugerido
	print ('{:<30}{:<10}'.format('Preço analisado:', converte_real(valor)))
	
	#dobro do preço
	print ('{:<30}{:<10}'.format('Dobro do preço:', dobro(valor)))
	
	#metade do preço
	print ('{:<30}{:<10}'.format('Metade do preço:', metade(valor)))
	
	#aumento em porcentagem
	print ('{:<30}{:<10}'.format('{}% de aumento:'.format(aumento), aumentar(valor, aumento)))
	
	#reducao em porcentagem
	print ('{:<30}{:<10}'.format('{}% de redução:'.format(reducao), diminuir(valor, reducao)))
	
	#fim
	print ('-'*40)
		
