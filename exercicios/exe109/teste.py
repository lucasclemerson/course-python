import moeda

preco = float(input('Digite um preço: '))
print ('A metade de {} é {}'.format(moeda.converte_real(preco), moeda.metade(preco)))
print ('O dobro de {} é {}'.format(moeda.converte_real(preco), moeda.dobro(preco)))
print ('Aumentando 10% de {} é {}'.format(moeda.converte_real(preco), moeda.aumentar(preco, 10, False)))
print ('Diminuir 20% de {} é {}'.format(moeda.converte_real(preco), moeda.diminuir(preco, 20, False)))

