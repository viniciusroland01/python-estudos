#Sorteando uma ordem na lista

from random import sample
a1=input('Nome do primeiro aluno: ')
a2=input('Nome do segundo aluno: ')
a3=input('Nome do terceiro aluno: ')
a4=input('Nome do quarto aluno: ')
lista=[a1,a2,a3,a4]
sorteio=sample(lista,len(lista))
print(f'A ordem foi: {sorteio[0]} em primeiro, {sorteio[1]} em segundo, {sorteio[2]} em terceiro e {sorteio[3]} por último.')


