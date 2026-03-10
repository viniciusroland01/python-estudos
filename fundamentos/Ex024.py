#Verificando as primeiras letras de um texto

#cidade=str(input('Qual o nome da cidade? '))
#cidade1=cidade.split()
#if cidade1[0].lower() == 'são'or'sao':
#    print('Positivo')
#else:
#    print('Negativo')

cid=str(input('Qual nome da cidade? ')).strip()
print(cid[:5].lower() == 'santo')