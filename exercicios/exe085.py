numeros = list()
pares = list()
impares = list()

for i in range(0,7):
	n = int (input('Qual número deseja guardar? '))
	if n % 2 == 0:
		pares.append(n)
	else:
		impares.append(n)	
	

numeros.insert(0, pares)	
numeros.insert(1, impares)

numeros[0].sort(reverse=True)
numeros[1].sort(reverse=True)

print ('\nNúmeros pares: ', end="")
for n in numeros[0]:
	print ('[{}]'.format(n), end=" ")

print ('\nNúmeros impares: ', end="")
for n in numeros[1]:
	print ('[{}]'.format(n), end=" ")
