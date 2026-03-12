#Detector de Palíndromo

texto=input('Digite alguma palavra ou frase: ')
for letra in range(len(texto)):
    if texto[letra] != texto[-(letra + 1)]:
        print('Não é palíndromo!')
        break
else:
    print ('É palíndromo!')





