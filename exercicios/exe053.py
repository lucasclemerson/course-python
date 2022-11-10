palavra = str(input('Digite uma palavra: '))
palavra_sem_espaco = palavra.replace(' ', '')
palavra_ao_contrario = str('')

for c in range(len(palavra_sem_espaco),0,-1):
	palavra_ao_contrario += palavra_sem_espaco[c-1];


print('PALAVRA CERTA: {}'.format(palavra_sem_espaco))
print('PALAVRA AO CONTRARIO: {}'.format(palavra_ao_contrario))

if palavra_ao_contrario == palavra_sem_espaco:
	print('É um políndromo')
else:
	print('Não é um políndromo')








