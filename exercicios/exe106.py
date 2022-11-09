from time import sleep

nome_do_sistema = 'SISTEMA DE GERENCIAMENTO DE BIBLIOTECAS'
pergunta_pesquisa = 'Digite a função que deseja encontrar? [exit]'
sair_do_programa = 'FIM DE EXECUÇÃO, ATÉ LOGO!'

largura = len(nome_do_sistema)+10


def titulo_padrao ():
	print ('\n{}+{}+'.format('\033[1;37;44m', '-'*largura))
	print ('|{}{}{}|'.format(' '*5, nome_do_sistema, ' '*5))
	print ('+{}+{}'.format('-'*largura, '\033[0;0m'))

	
def titulo_pesquisa():
	print ('{}+{}+'.format('\033[1;0;43m', '-'*largura))
	print (('|{}|'.format('{'+':^{}'.format(largura)+'}' )).format(pergunta_pesquisa), end="\033[0;0m ")
	funcao = str(input())
	print ('\033[1;0;43m+{}+{}'.format('-'*largura, '\033[0;0m'))
	return funcao


def efeito_pesquisa():
	print ('\033[1;32;40mProcurando rotina...\n[', end="")
	for i in range(0, largura):
		print ('=', end="", flush=True)			
		sleep(0.05) 
	print(']\033[0;0m')


def resultado_pesquisa(funcao):
	print ('{}+{}+'.format('\033[1;0;47m', '-'*largura))
	print (('|{}|'.format('{'+':^{}'.format(largura)+'}' )).format(str(help(funcao))), end="\033[0;0m ")	


def sair_programa():
	print ('{}+{}+'.format('\033[1;37;41m', '-'*largura))
	print (('|{}:'.format('{'+':^{}'.format(largura)+'}' )).format(sair_do_programa))
	print ('+{}+{}'.format('-'*largura, '\033[0;0m'))


while True:
	titulo_padrao()
	funcao = titulo_pesquisa()
	
	if funcao.upper() == 'EXIT':
		sair_programa()
		break;
	else:	
		efeito_pesquisa()
		resultado_pesquisa(funcao)
