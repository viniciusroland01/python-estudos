#Analisador de textos

nome=str(input('Qual é seu nome? '))
primeiro=nome.split()
print('Analisando seu nome. . . ')
print(f'Em maiúsculas {nome.upper()}')
print(f'Em minúsculas {nome.lower()}')
print(f'Ao todo seu nome tem {len(nome.replace(' ','').strip())} letras.')
print(f'O primeiro nome é {primeiro[0].capitalize()} e ele tem {len(primeiro[0])} letras.')
