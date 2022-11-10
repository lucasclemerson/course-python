from random import randint 
numeros = (randint(0,5,), randint(0,5,),randint(0,5,),randint(0,5,),randint(0,5,))
print(numeros)
menor = maior = numeros[0]

for n in numeros:
	if n > maior:
		maior = n

	if n < menor:
		menor = n

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
