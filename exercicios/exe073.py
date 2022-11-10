times = ('América-MG', 'Athletico', 'Atlético-GO', 'Atlético-MG', 'Avaí', 'Botafogo', 'Bragantino', 'Corinthians', 
	'Coritiba', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Juventude', 'Internacional', 'Palmeiras', 
	'Santos','São Paulo', 'Piracamjubá'
)

print('='*40)
print('{:^}'.format('OS 5 PRIMEIROS COLOCADOS'))
print('='*40)

for i in range(0,5):
	print (times[i])

print('='*40)
print('{:^}'.format('OS 4 ÚLTIMOS COLOCADOS'))
print('='*40)

for i in range(len(times)-4,len(times)):
	print (times[i])

print('='*40)
print('{:^}'.format('TODOS OS TIMES EM ORDEM ALFABETICA'))
print('='*40)

for i, t in enumerate(sorted(times)):
	print('[{}] - {}'.format((i+1), t))

print('='*40)
print('{:^}'.format('O TIME DO FLAMENGO SE ENCONTRA?'))
print('='*40)
print('NA POSIÇÃO #{}'.format(times.index('Flamengo')+1))
