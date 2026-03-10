#Primeiro e último nome da pessoa

nome=str(input('Digite seu nome: ')).strip().split()
print(f'O primeiro nome é {nome[0].title()} e o último nome é {nome[-1].title()}')


