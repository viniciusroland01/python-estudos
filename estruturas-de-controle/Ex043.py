#Índice de massa corporal

from colorama import init, Fore , Back
while True:
    init(autoreset=True)
    peso=input('Qual o peso em KG? ')
    if peso.lower() == 'sair':
        print(Fore.RED + 'Encerrando. . . ')
        break
    peso=float(peso)
    altura=float(input('Qual é a altura em metros? '))
    imc=peso/(altura**2)
    if peso <= 0 or altura <0:
        print('Número inválido!')
        continue
    if imc < 18.5:
        status= Fore.RED + 'ABAIXO DO PESO'
    elif 18.5 <= imc < 25:
        status= Fore.GREEN + 'PESO IDEAL'
    elif 25 <= imc < 30:
        status= Fore.MAGENTA + 'SOBREPESO'
    elif 30 <= imc < 40:
        status= Fore.MAGENTA + 'OBESIDADE'
    else:
        status= Fore.BLACK + Back.RED + 'OBESIDADE MORBIDA'
    print(f'Com sua altura {altura} e seu peso de {peso}kg seu IMC é {imc:.1f} e seu status de saúde é {status}')