lista = list()

for i in range(0,5):
	lista.append(int(input('Digite um número: ')))

copia = lista[:]
copia.sort()
menor = copia[0]
maior = copia[len(copia)-1]

print('Maior valor {}, posição {}'.format(maior, lista.index(maior)))
print('Menor valor {}, posição {}'.format(menor, lista.index(menor)))
