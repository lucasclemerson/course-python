media_idade = 0
idade_homem_mais_velho = 0
nome_home_mais_velhor = '';
mulheres_com_menos_de_20_anos = 0

for i in range(0,4):
	nome =  str(input('Informe seu nome: '))
	idade =  int(input('sua idade (anos): '))
	sexo =  str(input('e seu sexo (m/f): '))
	print('='*20)

	media_idade += idade

	if sexo == 'm' and idade > idade_homem_mais_velho:
		idade_homem_mais_velho = idade
		nome_home_mais_velhor = nome

	if sexo == 'f' and idade < 20:
		mulheres_com_menos_de_20_anos += 1

media_idade /= 4

print('A média de idade do grupo é {} anos'.format(media_idade))
print('Seu {} é o homem mais velho com {} anos de idade'.format(nome_home_mais_velhor, idade_homem_mais_velho))
print('O total de mulheres com menos de 20 anos foram {}'.format(mulheres_com_menos_de_20_anos))