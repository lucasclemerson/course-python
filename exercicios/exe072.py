extenso = (
	'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
	'onze', 'doze', 'treze', 'quatorze', 'quize', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
)

while True:
	n = int(input('Digite um número entre 0 e 20: '))
	if n > -1 and n < 21:
		print (f'O número escolhido foi o {extenso[n]}')
		break;
	else:
		print('Tente novamente.', end=" ")


