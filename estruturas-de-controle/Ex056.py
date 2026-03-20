#Analisador completo

soma_idade=0
media=0
maior_idade_homem=0
nome_velho=''
numero_mulheres=0
for i in range (1,5):
    print(f'----- {i}ª Pessoa -----')
    nome=input('Nome : ').strip()
    idade=int(input('Idade : '))
    soma_idade+=idade
    sexo=input('Sexo [M/F]: ').upper().strip()
    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem=idade
            nome_velho=nome
    if sexo == 'F':
        if idade < 20 :
            numero_mulheres+=1
media=(soma_idade/5)
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}.')
print(f'Ao todo são {numero_mulheres} mulheres com menos de 20 anos.')


