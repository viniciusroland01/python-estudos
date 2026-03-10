#Pintando parede

while True:
    larg=input('Qual a largura da parede? Ou "sair" para encerrar. ')
    if larg.lower()=='sair':
        print('Encerrando programa...')
        break
    else:
        try:
            larg1=float(larg)
            alt=input('Qual a altura da parede? ')
            alt1=float(alt)
            area=larg1*alt1
            tinta=area/2
            print(f'Essa parede tem dimensão de {larg1}X{alt1}, e área de {area}m².\nIrá precisar de {tinta} litros de tinta para pinta-lá.')
        except ValueError:
            print('Inválido!')


