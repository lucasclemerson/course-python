n = int(input('Informe um número inteiro: '))
ni = cont = 0
nf = acm =1

print('Sequência de Fibonacci')
while cont < n:
	print("[{}]".format(nf), end=" ")
	acm = nf
	nf = nf + ni 
	ni = acm
	cont += 1
