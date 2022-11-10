from random import randint 
sorteado = randint(1,10);

palpites = 0
jogada = -1

while jogada != sorteado:
	jogada = int(input('Digite um número: '))
	if jogada == sorteado:
		print('Você acertou!')
	else:
		print('Você errou!')
	palpites += 1

print('Número sorteado foi {}\nVocê utilizou {} palpites'.format(sorteado,palpites))