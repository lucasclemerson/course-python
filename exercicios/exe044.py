preco = float(input('Informe o preço do produto (R$): '))
print('='*50)
print('{:^50}'.format('Formas de pagamento'))
print('='*50)
print('Valor do produto: {:.2f} R$'.format(preco))
print('='*50)
print('1- Dinheiro/cheque (desconto 10%)\n2- Avista no cartão (desconto 5%)\n3- 2x no cartão (Valor normal)\n4- 3x ou mais no cartão (justo 20%)')
print('='*50)
forma_pagamento = int(input('Digite a opção de pagamento: '));

if forma_pagamento == 1:
    preco_final = preco - preco * .1; 
elif forma_pagamento == 2:
    preco_final = preco - preco * .05; 
elif forma_pagamento == 3:
    preco_final = preco    
elif forma_pagamento == 4:
    preco_final = preco + preco * .2; 
else:    
    preco_final = 0
    print('Forma de pagamento inválida')

print('='*50)
print('O valor final a ser pago pelo produto é {:.2f} R$'.format(preco_final))    
    




