#Par ou ímpar

from colorama import init, Fore
while True:
    init(autoreset=True)
    n=input(Fore.LIGHTCYAN_EX + 'Digite um número: ').lower()
    if n == 'sair':
        print(Fore.RED + 'Encerrando programa . . .')
        break
    n=int(n)
    if n%2 == 0:
        print(Fore.BLUE + 'Par')
    else:
        print(Fore.BLUE + 'Ímpar')