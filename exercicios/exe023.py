numero = int(6589)
milhar = int (numero/1000);
centena = int ((numero - 1000*milhar)/100);
dezena = int ((numero - 1000*milhar - 100*centena)/10);
unidade = int (numero - 1000*milhar - 100*centena -  10*dezena);

print ('Milhar: ', milhar)
print ('Centena: ', centena)
print ('Dezena: ', dezena)
print ('Unidade: ', unidade)

