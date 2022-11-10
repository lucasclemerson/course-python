from datetime import date

maior_idade = 0
menor_idade = 0

for i in range(1,8):
	ano = int(input('Digite o ano de seu nascimento: '))
	idade = date.today().year - ano
	if idade >= 21:
		maior_idade += 1
	else: 
		menor_idade += 1

print('Existem {} pessoas de maior idade,\ncom menor idade existem {}'.format(maior_idade, menor_idade))


