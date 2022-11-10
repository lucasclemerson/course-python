numeros = list()

while True:
	numeros.append(int(input('Digite um numero: ')))
	r = str(input('Deseja continuar? [S/N] ')).upper()
	if r == 'N':
		break
		
numeros.sort(reverse=True)

print('\nTotal de númros digitados foi {}'.format(len(numeros)))
print('Ordem decrescente dos valores: ', end="")
for i, v in enumerate(numeros):
	print('[{}]:{}'.format(i, v), end=" ")
if 5 in numeros:
	print('\nO valor 5 se enconta na lista na posição {}'.format(numeros.index(5)))	
else:
	print('\nO valor 5 não se enconta na lista')	