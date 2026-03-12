#Detector de Palíndromo

texto=input('Digite alguma palavra ou frase: ').replace(' ','')
inverso=texto[::-1]
print(f'O inverso de {texto.upper()} é {inverso.upper()}')
for letra in range(len(texto)):
    if texto[letra] != texto[-(letra + 1)]:
        print('Não é palíndromo!')
        break
else:
    print ('É palíndromo!')

'''texto=str(input('Digite alguma palavra ou frase: ')).strip().upper()
palavras = texto.split()
junto = ''.join(palavras)
inverso=''
for letra in range(len(junto) - 1, -1 ,-1 ):
   inverso += junto [letra]
if inverso == junto:
    print('É palíndromo!')
else:
    print('Não é palíndromo')'''


