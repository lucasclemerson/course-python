lista = [1,0,2,4,6]
ordem = list()

for item in lista:
	indexMenor = 0
	for item_2 in lista:
		if item_2 < item and item != item_2:
			indexMenor += 1

	ordem.insert(indexMenor, item)	
	indexMenor = 0

print (ordem)