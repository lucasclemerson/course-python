usuario = list()
usuario.append('Gustavo')
usuario.append(40)

galera = list()
galera.append(usuario[:])

usuario[0] = 'Maria'
usuario[1] = 35 
galera.append(usuario[:])

print (galera)


