n1 = int(input('Imforme N1: '))
n2 = int(input('Informe N2: '))

a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
r = n1 // n2
p = n1 ** n2

print ('{:=^50}'.format('Tabela de calcúlos'))
print('A soma {},\na subtração {},\na multiplicação {},\na divisão {:.3f}, \no resto da divisão {} e a potência {}'.format(a, s, m, d, r, p), end=' end \n')
print ('='*50)