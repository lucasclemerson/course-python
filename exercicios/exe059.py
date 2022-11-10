n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))

r = -1
while r != 5:
	print('='*50)
	print('[NÚMEROS] {}/{}'.format(n1,n2))
	print('[1] SOMAR')
	print('[2] MULTIPLICAR')
	print('[3] MAIOR')
	print('[4] NOVOS NÚMEROS')
	print('[5] SAIR')
	print('='*50)
	r  = int(input(':'))

	if r == 1:
		print ('A SOMA É {}'.format(n1+n2))
	elif r == 2:
		print ('A MULTIPLICAÇÃO É {}'.format(n1*n2))
	elif r == 3:
		maior = n1
		if maior < n2:
			maior = n2
		print ('O MAIOR NÚMERO0 É {}'.format(maior))	
	elif r == 4:
		n1 = int(input('Digite um novo valor para o número 1: '))
		n2 = int(input('Digite um novo valor para o número 2: '))
	elif r != 5:
		print ('Opção inexistente!')
print('fim')
