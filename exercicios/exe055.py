maior_peso = 0
menor_peso = 0

for i in range(0,5):
	peso = float(input('Digite um peso (Kg): '))

	if i == 0:
		maior_peso = peso
		menor_peso = peso
	
	if peso > maior_peso:
		maior_peso = peso

	if peso < menor_peso:
		menor_peso = peso

print('O maior peso foi {} Kg'.format(maior_peso))
print('O menor peso foi {} Kg'.format(menor_peso))
