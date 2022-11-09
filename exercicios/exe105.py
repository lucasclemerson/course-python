def notas (* n, situacao=False):
	retorno = {}
	retorno['total'] = len(n) 
	retorno['menor'] = n[0]
	retorno['maior'] = n[0]
	retorno['media'] = 0
	
	for i in n:
		if retorno['menor'] > i:
			retorno['menor'] = i
		if retorno['maior'] < i:
			retorno['maior'] = i
		retorno['media'] += i
	retorno['media'] = float(retorno['media'] / retorno['total'])

	if situacao == True:
		if retorno['media'] > 6:
			retorno['situcao'] = 'BOA'
		else:
			retorno['situcao'] = 'RUIM'
	return retorno

 
dicionario = notas(5,6,9,7,8,1, situacao=True)
print (dicionario)


