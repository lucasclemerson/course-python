def ficha (nome="<desconhecido>", gols=0):
	if (type(gols) != int):
		gols=0
	if len(nome) == 0:		
		nome="<desconhecido>"
	print ('O jogador {} marcou {} gols nesse campeonato'.format(nome, gols))

nome = str(input('Digite seu nome: '))
gols = input('Digite o total de gols que fez: ')
ficha(nome, gols)
