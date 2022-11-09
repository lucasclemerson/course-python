import funcoes

num = int (input('Digite um número: '))
f = funcoes.fatorial(num)
d = funcoes.dobro (num)
t = funcoes.triplo(num)

print ('O fatorial de {} é {}'.format(num, f))
print ('O dobro de {} é {}'.format(num, d))
print ('O triplo de {} é {}'.format(num, t))
