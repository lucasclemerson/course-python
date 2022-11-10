from datetime import date 
ano_atual = date.today().year
ano_nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - ano_nascimento

if idade < 18:
    print('Você tem {} anos\nEstá quase na hora de se alistar, faltam {} anos'.format(idade,18-idade))
elif idade > 45:
    print('Você tem {} anos\nJá passou da idade de se alistar, atraso de {} anos'.format(idade,idade-45))    
else:
    print('Você tem {} anos\nIdade suficiente para se alistar!'.format(idade))    