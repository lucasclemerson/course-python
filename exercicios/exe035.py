a = 5
b = 10
c = 9

i = (b-c) < a < (b+c)
ii = (a-c) < b < (a+c)
iii = (a-b) < c < (a+b)

print ('Condição 1: ', i)
print ('Condição 2: ', ii)
print ('Condição 3: ', iii)

if i and ii and iii:
	print ('Pode formar um triângulo!')
else:
	print ('Não pode formar um triângulo!')