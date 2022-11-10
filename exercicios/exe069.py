contador = 0
maiorIdade = totalHomem = mulherMenosVinte = 0

while True:
	print ('='*30)
	print (f'PESSOA NÚMERO [{contador}]')
	print ('='*30)
	sexo = str(input('INFORME O SEXO [M/F]:')).upper()
	idade = int(input('INFORME A IDADE: '))


	if idade > 18:
		maiorIdade = maiorIdade + 1
	if sexo == 'M':
		totalHomem = totalHomem + 1
	if sexo == 'F' and idade < 20:
		mulherMenosVinte = mulherMenosVinte + 1


	continuar = str(input('DESEJA CONTINUAR? [S/N]')).upper()
	if continuar == 'N':
		break
	contador = contador + 1

print ('\nFim de execução...')
print (f'O TOTAL DE PESSOAS COM MAIOR IDADE FORAM {maiorIdade} PESSOAS')	
print (f'O TOTAL DE {totalHomem} HOMENS')	
print (f'O TOTAL DE {mulherMenosVinte} MULHERES COM MENOS DE 20 ANOS DE IDADE')	