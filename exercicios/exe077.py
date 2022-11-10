palavras = ('APRENDER', 'ESTUDAR', 'TRABALHAR', 'EXECUTAR', 'ADMINISTRAR', 'PROGRAMDOR')
vogais = ('A', 'E', 'I', 'O', 'U')

for palavra in palavras:
	print (f'\n{palavra} contém as vogais: ', end="")

	for vogal in vogais:
		if vogal.upper() in palavra.upper():
			print('[{}]'.format(vogal), end="")
print()			