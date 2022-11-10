produtos = (
	'Maçã', 10.50,
	'Peito de Frango (1Kg)', 22.5,
	'Macarão do fino', 3.40,
	'Verduras', 15.89
)

print ('\n'+'=-='*15)
print ('{:^45}'.format('LISTAGEM DE PRODUTOS'))
print ('=-='*15)

for i in range (0, len(produtos), 2):
	print('{:.<27}R$ {:.>15}'.format(produtos[i], produtos[i+1]))
print ('=-='*15+'\n')