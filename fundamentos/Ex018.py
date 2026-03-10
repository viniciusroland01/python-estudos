#Seno, cosseno e tangente

from math import sin,cos,tan,radians
while True:
    a=input('Digite o valor do ângulo: ')
    if a.lower()=='sair':
        print('Encerrando. . .')
        break
    else:
        try:
            ang=float(a)
            ang1=radians(ang)
            seno=sin(ang1)
            cos=cos(ang1)
            tang=tan(ang1)
            print(f'O ângulo {ang} tem seno de {seno:.2f}, cosseno de {cos:.2f} e tangente de {tang:.2f}')
        except ValueError:
            print('Inválido!')


