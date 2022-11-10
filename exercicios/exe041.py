from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
idade = ano_atual - ano_nascimento

if idade < 0:
    print('Idade Inválida!')
elif idade <= 9:
    print('Mirim!')
elif idade <= 14:
    print('Infantil')   
elif idade <= 19:
    print('Junior')  
elif idade == 20:
    print('Sênior!')
else:
    print('Master!')         
