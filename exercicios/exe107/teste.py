import moeda

preco = float(input('Digite um preço: '))
print ('A metade de {} é {}'.format(preco, moeda.metade(preco)))
print ('O dobro de {} é {}'.format(preco, moeda.dobro(preco)))
print ('Aumentando 10% de {} é {}'.format(preco, moeda.aumentar(preco, 10)))
print ('Diminuir 20% de {} é {}'.format(preco, moeda.diminuir(preco, 20)))

