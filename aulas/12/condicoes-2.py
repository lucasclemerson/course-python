nome = str(input('Digite um nome: '))

if nome in 'Clemerson':
   print('Que nome bonito!')
elif nome in 'Carlos Maria Paulo João':
    print('Seu nome é bem popular!')
else:
    print('Seu nome é diferente')

print ('Tenha um bom dia {}!'.format(nome))
