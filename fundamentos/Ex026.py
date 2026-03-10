#Primeira e última ocorrência de uma string

frase=input('Digite uma frase: ').strip().lower()
print(f'A letra "a" aparece {frase.count('a')} vezes.')
print(f'A primeira letra "a" aparece na posição {frase.find('a')+1}')
print(f'A última vez que a letra "a" aparece é na posição {frase.rfind('a')+1}')