preco_atual = float(input('Informe o preço do produto (R$): '))
preco_com_desconto = preco_atual - (preco_atual*0.05)
print ('Valor final será de {:.2f} R$'.format(preco_com_desconto))