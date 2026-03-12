#Contagem regressiva

from time import sleep
from colorama import init,Fore
init(autoreset=True)
print('><'*8)
print(Fore.YELLOW + '10 segundos para 2027!')
print('><'*8)

sleep(1)

input('Aperte enter para começar.')

for c in range (10,-1,-1):
    print(c)
    print('')
    sleep(1)
print(Fore.LIGHTYELLOW_EX + '\U0001F389FELIZ 2027!\U0001F389 ')
sleep(1)
print('')
print(Fore.RED + '\U0001F387BUM BUM! POOOOOW!\U0001F387' )