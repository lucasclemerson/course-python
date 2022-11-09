def maior(numeros):
	print ('Números digitados: {}'.format(numeros))
	numeros.sort(reverse=True)
	if len(numeros) == 0:
		print ('Você não digitou nenhum número')
	else:
		print ('O maior número do conjunto é {}'.format(numeros[0]))


def titulo (msg):
	print ('-'*len(msg))
	print (msg)
	print ('-'*len(msg))


titulo('PROCURANDO O MAIOR NÚMERO')
lista = []

while True:
	n = int (input('Digite um número: [999 para sair] '))
	if n != 999:
		lista.append(n)
	else:
		break	

maior (lista)
