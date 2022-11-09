from datetime import date

def voto (ano):
	global idade
	situacao = 'OPCIONAL'
	idade = date.today().year - ano
	if idade < 16:
		situacao = 'NEGADA'
	elif idade < 45 and idade >= 16:
		situacao = 'OBRIGATÓRIO'

	return situacao



idade = 0 
nasc = int(input('Informe o ano de nascimento: '))
situcao = voto(nasc)
print ('Com {} anos de idade, seu voto é {}'.format(idade, situcao))


