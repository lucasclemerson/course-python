from math import sin, cos, tan, radians
angulo = float(input('Digite um ângulo°: '))
angulo = radians(angulo)
s = sin(angulo)
c = cos(angulo)
t = tan(angulo)

print ('SENO: {:.2f}\nCOSENO: {:.2f}\nTANGENTE: {:.2f}'.format(s,c,t))
