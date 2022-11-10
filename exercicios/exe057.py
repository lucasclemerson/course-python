s = ''
while s != 'M' and s != 'F':
	if s != '':
		print('Sexo inválido!')
	s = str(input('Informe o seu sexo: [M/F]')).upper()

print('Seu sexo é {}'.format(s))