from random import randint

lista = []

def titulo (msg):
	print ('-'*len(msg))
	print (msg)
	print ('-'*len(msg))


def soma (numeros):
	soma=0
	for i in numeros:
		soma += i
	titulo('A soma dos valores pares foi {}'.format(soma))	
		
def sortear():
	titulo ('SORTEADO NÙMEROS ALEATÓRIOS')
	lista = [randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10)]
	print ('Números sorteados: {}'.format(lista))
	soma (lista)
	
	
sortear()
