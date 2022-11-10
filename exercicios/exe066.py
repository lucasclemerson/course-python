soma = 0
total = 0
r = 0;

print('[999] para sair')
while True:
	r = int(input('Digite um número: '))
	if r == 999:
		break	
	soma = soma + r
	total = total + 1

print('\nO total de números digitados foram {}'.format(total))
print('A soma de todos os números foi {}'.format(soma))		
