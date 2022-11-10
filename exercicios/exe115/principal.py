import menu
import pessoa

lista = list()

while True:	
	opcao = menu.cabecario()

	#listar pessoas
	if opcao == 1:
		lista = pessoa.listar()
		menu.listar_pessoas(lista)
		
	#cadastar
	if opcao == 2:
		lista = menu.cadastar_pessoas()
		pessoa.cadastrar(lista)

	#sair
	if opcao == 3:
		break
	
menu.sair()
