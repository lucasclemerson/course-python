def init (msg):
	print ('-'*40)
	print ('{:^40}'.format(msg))
	print ('-'*40)


def calcular_area(c, l):
	area = c * l
	print ('\nA área do seu terreno {} x {} é de {} m²'.format(l,c,area))


init ('Calculando Área de terrenos')
largura = float(input('largura (m): '))
comprimento = float(input('comprimento (m): '))
calcular_area(c=comprimento, l=largura)
