#Cateto e hipotenusa

from math import pow, sqrt
while True:
    c=input('Cateto adjacente: ')
    if c.lower()=='sair':
        print('Encerrando programa . . .')
        break
    else:
        try:
            ca=float(c)
            co=float(input('Cateto oposto: '))
            hip=sqrt((pow(ca,2))+(pow(co,2)))
            '''hip=sqrt((ca**2)+(co**2))'''
            print(f'O valor da hipotenusa desse triângulo é {hip:.2f}')
        except ValueError:
            print('Inválido. . . ')

