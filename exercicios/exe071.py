print('='*40)
print('{:^40}'.format('TELA INICIAL DO BANCO'))
print('='*40)
valor = int(input('DIGITE O VALOR QUE DESEJA SACAR (R$): '))
cedulas = [50,20,10,1]
quantidade = [0,0,0,0]

contador = 0
while contador < len(cedulas):
	quantidade[contador] = valor // cedulas[contador]
	valor = valor - (quantidade[contador]*cedulas[contador]) 
	contador = contador + 1


for i in range(0,len(quantidade)):
	print('{},00 R$  = {}'.format(cedulas[i], quantidade[i]))
