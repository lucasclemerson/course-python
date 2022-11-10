n = int(input('informe um número: '))
c = 1
r = 1
while c <= n:
	r = c * r
	c += 1

print ('O fatorial de {} é {}'.format(n, r))
