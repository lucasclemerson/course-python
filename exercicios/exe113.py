n = f = 0

while True:
	#numero inteiro
	try:
		n = int(input('Digite um número inteiro: '))
	except Exception as ValueError:
		print ('Número inteiro inválido. ', end='')		
	except Exeception as KeyboardInterrupt:
		print ('O usuário preferiu não informar')
	else:
		break
	
while True:
	#numero float
	try:
		f = float(input('Digite um número flutuante: '))
	except Exception as ValueError:
		print ('Número flutuante inválido. ', end='')		
	except Exeception as KeyboardInterrupt:
		print ('O usuário preferiu não informar')
	else:
		break		
	
	
print ('O número inteiro digitado foi {}'.format(n))	
print ('O número flutuante digitado foi {}'.format(f))		
		
