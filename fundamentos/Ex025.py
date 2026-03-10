#Procurando uma string dentro de outra

nome = str(input('Qual é o seu nome?').lower().strip())
print(f'Seu nome tem Silva? {'silva' in nome}')