def fatorial (n=1, show=False):
	"""
	param show: é responsavel por mostrar ou não o calculo da função
	param n: é o número que o usuário deseja o fatorial
	return: null
	"""

	cont = n	
	calculo = ''
	r=1 
	while cont > 0:
		r *= cont		
		if show == True:	
			calculo += str(cont) 		
			if (cont-1) != 0:
				calculo += ' x '
			else:
				calculo += ' = '
		cont -= 1
	print ('{}{}'.format(calculo, r))


n = int(input('Digite um número: '))
show = str(input('Deseja mostrar o calculo? [s/n] ')).upper()

if show == 'S':
	show = True
else:
	show = False

fatorial(n, show)
print(help(fatorial))
