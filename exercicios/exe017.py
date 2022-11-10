from math import pow, sqrt
a = int(input('Digite o valor do cateto A: '))
b = int(input('Digite o valor do cateto B: '))

h = pow(a, 2) + pow(b, 2)
h = sqrt(h)

print ('O valor da hipotenusa é {:.2f}'.format(h))