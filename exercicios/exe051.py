a1 = int(input('Informe um número 1º PA: '))
r = int(input('Informe a razão da progressão: '))
c = int(1)
for i in range(a1, a1+10*r,r):
    print('A{} = {}'.format(c, i))
    c+=1