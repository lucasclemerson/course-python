a = int(input('Informe o valor do lado A: '))
b = int(input('Informe o valor do lado B: '))
c = int(input('Informe o valor do lado C: '))

i = (b-c) < a < (b+c)
ii = (a-c) < b < (a+c)
iii = (a-b) < c < (a+b)

print ('Condição 1: ', i)
print ('Condição 2: ', ii)
print ('Condição 3: ', iii)

if (i and ii and iii):
    if (a==b and b==c):
        print('Seu triângulo é equilátero') 
    elif (a==b or a==c or b==c):
        print('Seu triângulo é Isósceles')
    else:    
        print('Seu triêngulo é escaleno')    
else:
	print ('Não pode formar um triângulo!')