numero =  int(input('Informe um número: ')) 
print('1- binário\n2- octal\n3- hexadecimal')
print('='*50)
opcao = int(input('Informe a conversão[1/2/3]: '))


if opcao == 1:
    print('Convertido para binário: {}'.format(format(numero, 'b')))
elif opcao == 2:
	print('Convertido para octal: {}'.format(format(numero, 'o')))
elif opcao == 3:
	print('Convertido para hexadecimal: {}'.format(format(numero, 'x')))
else:
    print('Opção inválida!')
