from time import sleep
from random import randint
pc = randint(1, 3)
print('='*50)
print(pc)
print('='*50)
print('{:^50}'.format('Informe sua jogada'))
print('='*50)
print('1- Pedra\n2- Papel\n3- Tesoura')
print('='*50)
jogada = int(input('>>> '))

print('='*50)
print('Analisando jogada...')
sleep(3)
print('='*50)


#empate
if pc == jogada:
    print('Resultado >>> EMPATE')

elif jogada == 1:
    if pc == 3:
        print('Resultado >>> VOCÊ VENCEU')
    else:
        print('Resultado >>> VOCÊ PERDEU')
        
elif jogada == 2:
    if pc == 1:
        print('Resultado >>> VOCÊ VENCEU')
    else:
        print('Resultado >>> VOCÊ PERDEU')       

elif jogada == 3:
    if pc == 2:
        print('Resultado >>> VOCÊ VENCEU')
    else:
        print('Resultado >>> VOCÊ PERDEU') 
else :
    print('Resultado >>> Erro com as jogadas')
    
#print("VOCÊ: ", jogada)
#print("PLAYER 1: ", pc)    
    
    
    
    


