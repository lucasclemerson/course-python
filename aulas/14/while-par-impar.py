r = 'S'
p = 0
i = 0
while r == 'S':
	n = int(input('Informe um número: '))
	if n % 2 == 0:
		p += 1
	else: 
		i += 1	
	r = str(input('Deseja continuar? [S/N]')).upper()

print('O total de números pares foi {} e {} impares'.format(p,i))