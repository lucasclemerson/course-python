from math import pow

peso = float(input('Infrome seu peso em Kg: '))
altura = float(input('Informe sua altura em metros: '))
imc = peso / pow(altura, 2)

print('Seu IMC é {:.3f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal!')
elif imc >= 25 and imc < 30:
    print('Sobrepeso!')     
elif imc >= 30 and imc < 40:
    print('Obesidade')
elif imc > 40:
    print('Obesidade mórbida')        

