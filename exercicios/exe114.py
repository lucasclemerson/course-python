import urllib
import urllib.request

try:
	site = str(input('search your site: '))
	urllib.request.urlopen(site)
except Exception as erro:
	print ('ERRO:{}'.format(erro.__class__))	
else:
	print ('Site está disponivel!')
