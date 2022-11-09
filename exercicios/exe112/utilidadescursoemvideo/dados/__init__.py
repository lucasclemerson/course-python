def lerDinheiro(msg=''):
	retorno = ''
	while True:
		valor = str(input(msg))
		for v in range(0, len(valor)):
			if valor[v].isnumeric():
				retorno += valor[v]
			elif valor[v] == '.' or valor[v] == ',':
				retorno += '.'
		
		if len(retorno) == 0:
			retorno=''
			print ('\033[1;31m')
			print ('"{}" não é um valor válido.\033[0;0m '.format(valor))	
		
		elif isinstance(float(retorno), float):
			break;
	return float(retorno)
	
