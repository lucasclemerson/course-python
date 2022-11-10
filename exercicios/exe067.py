while True:
	print('='*40)
	n = int(input('Digite um número: '))
	if n < 0:
		break

	print('='*40)
	for i in range (1,11):
		multi = n * i
		print (f'{n} X {i} = {multi}')	
print('\nFim')
