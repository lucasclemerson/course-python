print ('Informe a expressão matematica...')
expressao = list(input('>>> '))
print ('>>>')

print ('Total de parenteses (: {}'.format(expressao.count('(')))
print ('Total de parenteses ): {}'.format(expressao.count(')')))

condicao = expressao.count(')') == expressao.count('(')
if condicao:
	print ('Expressão válida!')
else:
	print('Expressão inválida!')