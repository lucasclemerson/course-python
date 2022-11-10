soma = total = media = 0
menor = maior = 0
valor = contador = 0
r = 'S'

while r == 'S':
	if r == 'S':
		valor = int(input('Digite um número: '))
		soma += valor
		total += 1

		'''calculando o valor menor e maior'''
		if contador == 0:
			maior = valor
			menor = valor
			contador +=1 
		if maior < valor:
			maior = valor
		if menor > valor:
			menor = valor
	r = str(input('Deseja continuar? [S/N]\n: ')).upper()

media = float(soma/total)

print('\nFim de execução...')
print('O maior valor fornecido foi {}'.format(maior))
print('O menor valor fornecido foi {}'.format(menor))
print('A média dos valores fornecidos foi {:.2f}'.format(media))		
