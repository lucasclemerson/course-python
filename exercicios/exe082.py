numeros = pares = impares = list()

while True:
	n = int(input('Digite um numero: '))
	numeros.append(n)
	r = str(input('Deseja continuar? [S/N] ')).upper()
	if r == 'N':
		break
		
pares = numeros[:]
impares = numeros[:]

for n in numeros:
	if n % 2 != 0:
		pares.remove(n)
	else:
		impares.remove(n)	


print('\nGRUPO PAR:', end=" ")
for n in pares:
	print(f'[{n}]', end="") 

print('\nGRUPO IMPARES:', end=" ")
for n in impares:
	print(f'[{n}]', end="") 

print('\nGRUPOS PAR + IMPAR', end=" ")
for n in numeros:
	print(f'[{n}]', end="") 