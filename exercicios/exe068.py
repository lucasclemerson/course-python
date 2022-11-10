from random import randint

vitorias = 0

while True:
	pc = randint(0,5)

	print('='*40)
	print('BRINCANDO DE PAR OU IMPAR')
	print('='*40)
	opcao = str(input('ESCOLHA [P/I]:')).upper()
	print('='*40)
	j = int(input('DIGITE O VALOR: '))
	print('='*40)
	print (f'PLAYER 1: {pc}')

	soma = pc + j
	if (opcao=='P' and soma%2==0) or (opcao=='I' and soma%2!=0):
		print ('WINX, VOCÊ GANHOU!')
		vitorias += 1
	else:
		print ('BROTHER, VOCÊ PERDEU!')
		break

print(f'TOTALIZANDO {vitorias} VITÓRIA(S)')