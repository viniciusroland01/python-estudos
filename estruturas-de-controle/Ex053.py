#Detector de Palíndromo

s=0
for i in range (1,500):
    impares= [i % 2 != 0 and i/3 == 0]
    s+=impares
    print(s)

