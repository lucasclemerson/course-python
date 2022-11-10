cores = {}
cores['azul'] = '\033[1;34m' 
cores['branco'] = '\033[1;37m' 
cores['amarelo'] = '\033[1;33m' 
cores['vermelho'] = '\033[1;31m' 
cores['fim'] = '\033[0;0m'


def cabecario ():
	while True:
		try:
			#titulo
			print ('\n')
			print ('-'*40)
			print ('{:^40}'.format('MENU PRINCIPAL DA APLICAÇÃO'))
			print ('-'*40)

			#opções
			opcoes = ['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema']
			for i, o in enumerate(opcoes):
				print ('{}{} -{} {}{}{}'.format(cores['amarelo'],(i+1),cores['fim'],cores['azul'],o,cores['fim']))
			print ('-'*40)
			opcao = int(input('{}{}{}'.format(cores['amarelo'], 'Escolha um opção: ', cores['fim'])))
		
			if opcao in (1,2,3):	
				return opcao
			else:
				opcao_invalida()	
		except Exception as ValueErro:
			opcao_invalida()	
			
			
def cadastar_pessoas():
	retorno = []
	#titulo
	print ()
	print ('-'*40)
	print ('{}{:^40}{}'.format(cores['amarelo'], 'CADASTRAR UMA NOVA PESSOA', cores['fim']))
	print ('-'*40)
	
	while True:
		try: 
			nome = str(input('DIGITE O NOME: '))
			idade = int(input('AGORA A IDADE: '))
			retorno.append({'nome':nome, 'idade':idade})
		except Exception as KeyboardInterrupt:
			print ('\nPOR FAVOR, INFORME OS DADOS CORRETAMENTE!\n')
		
		except Exception as ValueErro:
			dados_invalidos()
		else:
			print ()
			resposta = str(input('DESEJA CADASTRAR MAIS PESSOAS? [S/N] ')).upper()
			if resposta == 'N':
				break
			else:
				print('\n')
				
	print ('\nOS DADOS FORAM GRAVADOS COM SUCESSO!\n')
	return retorno[:]
			
			

def listar_pessoas(pessoas):
	#titulo
	print ()
	print ('-'*40)
	print ('{}{:^40}{}'.format(cores['amarelo'], 'PESSOAS JÁ CADASTRADAS NO SISTEMA', cores['fim']))
	print ('-'*40)
	print ('{:^10}{:^20}{:^10}'.format('#', 'NOME', 'IDADE'))
	print ('-'*40)

	for i, p in enumerate(pessoas):
		print ('{:^10}{:^20}{:^10}'.format(i, p['nome'], p['idade']))			
	print ('-'*40+'\n')
				

def opcao_invalida():
	print (cores['vermelho'])
	print ('-'*40)
	print ('{:^40}'.format('OPÇÃO SELECIONADA É INVÁLIDA'))
	print ('-'*40)
	print (cores['fim'])


def dados_invalidos():
	print (cores['vermelho'])
	print ('-'*40)
	print ('{:^40}'.format('DADOS INVÁLIDOS, TENTE NOVAMENTE.'))
	print ('-'*40)
	print (cores['fim'] + '\n\n')
	

def sair ():
	print (cores['azul'])
	print ('-'*40)
	print (cores['fim'])
	print ('{}{:^40}{}'.format(cores['branco'], 'FIM DE EXECUÇÃO, ATÉ MAIS!', cores['fim']))
	print (cores['azul'])
	print ('-'*40)
	print (cores['fim'])
