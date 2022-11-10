n = int(input('Digite um número: '))
contador = 0

for i in range(1,n+1):
	if n % i == 0:
		contador += 1   
if n==1 or n==2 or contador == 2:
    print('É primo')
else:
    print('Não é primo')            