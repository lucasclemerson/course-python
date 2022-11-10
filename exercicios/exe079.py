numeros = list()

while True:
	n = int(input('Digite um número: '))
	if n in numeros:
		print('Número já adicionado, tente outro.')
	else:
		numeros.append(n)
		print('Número adicionado com sucesso.')
		r = str(input('Deseja sair? [S/N] '))
		if r.upper() == 'S':
			break	

print ('Os valores digitados foram: ', end="")
numeros.sort()
for n in numeros:
	print (f'[{n}]', end="")
