a1 = int(input('Informe um número 1º PA: '))
r = int(input('Informe a razão da progressão: '))
final = a1 + 10 * r
c = 1

while a1 < final:
	print('A{} = {}'.format(c, a1))
	a1 += r
	c += 1