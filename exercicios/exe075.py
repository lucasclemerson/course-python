n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))

numeros = (n1, n2, n3, n4)
		
print('\nVocê digitou os valores {}'.format(numeros))		
print(f'\nApareceu {numeros.count(9)} nove(s)')

if 3 in numeros:
	print(f'Primero valor três apareceu na {numeros.index(3)} posição')
else:
	print('O número três não foi encontrado em nenhuma posição')


print('Os números pares digitados foram: ', end="")
for n in numeros:
	if n %  2 == 0:
		print('[{}]'.format(n), end=' ')