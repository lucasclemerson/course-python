dado = list()
galera = list()


while True:
	dado.append(str(input('Informe o nome: ')))
	dado.append(float(input('Informe o peso: ')))
	galera.append(dado[:])
	dado.clear()

	r = str(input('Deseja continuar? [s/n] ')).split()[0].upper()
	if r == 'N':
		break;

pessoa_pesada = []
pessoa_leve = []

for index, pessoa in enumerate(galera):
	if pessoa[1] > 100:
		pessoa_pesada.append(pessoa)
	else:
		pessoa_leve.append(pessoa)
		

print (galera)
print ('\nForam {} pessoa(s) cadastrada(s)'.format(len(galera)))
print (f'A(s) pessoa(s) com o maior peso foram ', end="")

for i in pessoa_pesada:
	print ('[{}]'.format(i[0]), end=" ")
print('com mais de 100KG')


print (f'A(s) pessoa(s) com o menor peso foram ', end="")
for i in pessoa_leve:
	print ('[{}]'.format(i[0]), end=" ")
print('com menos de 100KG')
