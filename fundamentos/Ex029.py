#Velocidade do carro

from colorama import Fore, init
while True:
    init(autoreset=True)
    vel=input('Qual a velocidade do carro? ')
    if vel.lower() == 'sair':
        print('Encerrando programa')
        break
    vel=float(vel)

    if vel > 80:
        print(Fore.LIGHTRED_EX + f'Você foi multado por passar a {vel}km/h.')
        print(Fore.LIGHTRED_EX + f'A multa ficou no valor de: R$ {(vel-80)*7:.2f}')
    else:
        print(Fore.LIGHTGREEN_EX + 'Dentro dos limites da via, dirija com segurança!')
    print('Tenha um bom dia! Dirija com segurança!')



