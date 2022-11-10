delimitador = ':'
caminho = 'dados.txt'

def listar ():
	retorno = list()
	with open(caminho, 'r', encoding='utf-8') as arquivo:
		dados = arquivo.read()
	pessoas = dados.split('\n')
	for p in pessoas:
		try:
			dado = {'nome':p.split(delimitador)[0], 'idade':p.split(delimitador)[1]}
			retorno.append(dado.copy())
			dado.clear()
		except Exception as IndexError:	
			break
						
	return retorno



def cadastrar (lista=[]):
	arquivo = open(caminho, 'a')
	pessoas =  list()
	
	for p in lista:
		nome = p['nome']
		idade = p['idade']
		pessoas.append('{}{}{}\n'.format(nome, delimitador, idade))		
		
	arquivo.writelines(pessoas)	
