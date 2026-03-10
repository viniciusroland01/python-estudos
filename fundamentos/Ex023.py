#Separando dígitos de um número

numero = int(input('Digite um número de 0 a 9999: '))
if numero >= 10000:
    print('O número ultrapassou 9999!')
elif numero <= 0:
    print('O número é menor que 0!')
else:
    print(f'Analisando o número {numero}. . . ')
    print(f'Unidade = {numero%10}')
    print(f'Dezena = {(numero//10)%10}')
    print(f'Centena = {(numero//100)%10}')
    print(f'Milhar = {(numero//1000)%10}')