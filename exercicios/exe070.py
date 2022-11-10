contador = 0
valorTotal = produtosMaiorMil = 0
nomeProdutoBarato = ''

while True:
	print ('='*30)
	print (f'PRODUTO NÚMERO [{contador}]')
	print ('='*30)
	nome = str(input('INFORME O NOME:'))
	preco = float(input('INFORME o PREÇO: '))

	valorTotal += preco
	if preco > 1000:
		produtosMaiorMil += 1

	'''produto mais barato'''
	if contador == 0:
		precoProdutoBarato = preco
		nomeProdutoBarato = nome

	elif preco < precoProdutoBarato:
		precoProdutoBarato = preco
		nomeProdutoBarato = nome



	continuar = str(input('DESEJA CONTINUAR? [S/N]')).upper()
	if continuar == 'N':
		break
	contador = contador + 1

print ('\nFim de execução...')
print ('O VALOR TOTAL DOS PRODUTOS FOI {:.2f} R$'.format(valorTotal))
print (f'O TOTAL DE PRODUTOS COM VALOR MAIOR QUE 1.000,00 R$ FORAM {produtosMaiorMil}')
print ('O PRODUTO MAIS BARATO FOI O(A) {}, CUSTANDO {:.2f} R$'.format(nomeProdutoBarato, precoProdutoBarato))