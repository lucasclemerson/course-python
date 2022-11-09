def leiaint (text=''):
	while True: 
		n = str(input(text))
		if n.isnumeric():
			break
		else:
			print ('{} - Tente novamente.'.format(type(n)), end=" ")
	return n

numero = leiaint('Informe um valor inteiro:')
