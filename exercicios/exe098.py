from time import sleep

def contador (i, f, a):	
	sequencia = []	
	if i < f:
		print ('-'*40)
		print ('Contagem de {} até {} em {}'.format(i,f,a))
		print ('-'*40)
		for cont in range (i, f, a):
			sequencia.append(cont)
	else:
		print ('-'*40)
		print ('Contagem de {} até {} em {}'.format(i,f,a))
		print ('-'*40)
		for cont in range (f, i, a):
			sequencia.append(cont)
			sequencia.sort(reverse=True)			
	
	print ('Sequência:', end=" ")
	for n in sequencia:
		print (n, end=" ", flush=True)
		sleep(1)			
	print ('\n')


contador(1,10,1)
contador(10,0,2)


while True:
	print ('-'*40)
	i = int (input('Ponto de partida: [999 fim] '))

	if i != 999:
		f = int (input('Ponto de chegada: '))
		a = int (input('Contar quantos saltos por vez? '))
		contador(i,f,a)
	else:
		break
