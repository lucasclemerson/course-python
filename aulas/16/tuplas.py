produtos = ('Cabo', 'Conector', 'Roteador', 'ONU')
pratos = ('Lasanha', 'Panqueca', 'Macaronada', 'Creme de Galinha') 


for produto in produtos:
	print(produto) 

for i in range(0, len(pratos)):
	print(f'Comida #{i} - {pratos[i]}')

for index, equipamento in enumerate(produtos):
	print('#{} - {}'.format(index, equipamento))


del (produtos)
