#Aumentos múltiplos

while True:
    salario=input('Qual o salário do funcionário? R$')
    if salario.lower()=='sair':
        print('Encerrando. . . ')
        break
    try:
        salario=float(salario)
        if salario > 1250:
            novo=(10/100*salario)+salario
        else:
            novo=(15/100*salario)+salario
        print(f'O novo salário é R${novo:.2f}')
    except ValueError:
        print('Inválido')


