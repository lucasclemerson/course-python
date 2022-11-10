console = input('Infome um número: ')
numero = int (console)
print('\n{:=^30}\n'.format('Tábuda do ' + console))

for c in range(0,11):
    print ('{} x {} = {}'.format(numero, c, numero*c))

print(30*'=')