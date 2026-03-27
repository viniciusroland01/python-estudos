#Validação de dados

'''while True:
    sexo=input('Qual o seu sexo? ').strip().upper()[0]
    if sexo == "M"  or sexo == "F" :
        print(f'Sexo {sexo} salvo com sucesso!')
        break
    else :
        print('Só é aceito as letras "M" ou "F".')'''

sexo = input('Qual o seu sexo? ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input(('Dados inválidos, por favor informe seu sexo: (M/F)')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')





