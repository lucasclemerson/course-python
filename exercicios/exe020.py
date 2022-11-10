from random import shuffle
a1 = str(input('Infome o nome do 1º aluno: '))
a2 = str(input('Infome o nome do 2º aluno: '))
a3 = str(input('Infome o nome do 3º aluno: '))
a4 = str(input('Infome o nome do 4º aluno: '))

alunos = [a1,a2,a3,a4]
shuffle(alunos)

print('A ordem de apresentação será')
print(alunos)

