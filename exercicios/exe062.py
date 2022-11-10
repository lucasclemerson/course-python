a1 = int(input('Informe um número 1º PA: '))
r = int(input('Informe a razão da progressão: '))
final = a1 + 10 * r
c = 1

while a1 < final:
	print('A{} = {}'.format(c, a1))
	a1 += r
	c += 1


q = 1
while q != 0:
	print ('Para sair, basta digitar [0]')
	q = int(input('Quantos ainda deseja mostrar?'))

	if r != 0:
		final = a1 + q * r 
		while a1 < final:
			print('A{} = {}'.format(c, a1))
			a1 += r
			c += 1


print('\nfim')