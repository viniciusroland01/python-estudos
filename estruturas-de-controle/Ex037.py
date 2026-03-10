#Conversor de base númerica

'''while True:
    n1 = input('Digite um número para saber sua conversão: ')
    if n1.lower() == 'sair':
        print('Encerrando . . . ')
        break
    n1=int(n1)
    conversao = str(input('Qual será a base de conversão? (binário, octal, hexadecimal)')).strip()
    binario = ''
    octal = ''
    hexa = ''
    if conversao.lower() == 'binario' or conversao.lower() == 'binário':
        while n1 > 0:
            resto = n1 % 2
            binario = str(resto) + binario
            n1 = n1 // 2
        print(binario)
    elif conversao.lower() == 'octal':
        while n1 > 0:
            resto = n1 % 8
            octal = str(resto) + octal
            n1 = n1// 8
        print(octal)
    elif conversao.lower() == 'hexadecimal' or conversao.lower() == 'hexa':
        resultado = ''
        hex_decimal = {
            10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
        }
        while n1 > 0:
            resto = n1 % 16
            if resto >= 10:
                hexa = hex_decimal[resto]
            else:
                hexa = str(resto)
            resultado = hexa + resultado
            n1 = n1 // 16
        print(resultado)'''

while True:
    n1=input('Digite um número inteiro: ')
    if not n1.isnumeric():
        print('Inválido. . . ')
        continue
    print('''Escolha uma opção para conversão:
    [1] BINÁRIO
    [2] OCTAL
    [3] HEXADECIMAL
    [4] SAIR''')
    resposta=input('Qual opcão? ')
    n1=int(n1)
    if resposta == '4':
        print('Encerrando . . . ')
        break
    elif resposta == '1':
        nome='BINÁRIO'
        conversao=bin(n1)
    elif resposta == '2':
        nome='OCTAL'
        conversao=oct(n1)
    elif resposta == '3':
        nome='HEXADECIMAL'
        conversao=hex(n1)
    else:
        print('Inválido')
        continue
    print(f'A conversão do número {n1} para {nome} é {conversao[2:]}')




