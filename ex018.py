from math import radians,sin,cos,tan
ang = float(input('Digite um angulo: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print(f'O angulo {ang} tem sen {seno:.2f}, cos {cosseno:.2f}, tan {tangente:.2f}')