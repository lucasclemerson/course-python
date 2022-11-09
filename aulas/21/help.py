def contador(i, f, p):
	"""
	:param i: inicio da contagem
	:param f: fim da contagem
	:param p: pula a quantidade desejada até chegar ao fim
	"""
	
	c=i
	while c <= f:
        print ('{} '.format(c), end="")
        c+=p
    print ('FIM!')
	

