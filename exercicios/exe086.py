from random import randint 

matriz = list()

for i in range (0,3):
	linhas = list()
	for j in range (0,3):
		#print ('Digite o valor para [{}][{}]:'.format(i,j), end=" ")
		linhas.insert(j, randint(0,20))
	matriz.insert(i, linhas)

print('='*40)
for i in range (0,3):
	for j in range (0,3):
		print('[ {} ]'.format(matriz[i][j]), end=" ")
	print ()