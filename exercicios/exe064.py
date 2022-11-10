soma = 0
total = 0

r = 0;

print('[999] para sair')
while r != 999:
	r = int(input('Digite um número: '))
	if r != 999:
		soma = soma + r
		total = total + 1

print('\nO total de números digitados foram {}'.format(total))
print('A soma de todos os números foi {}'.format(soma))		
