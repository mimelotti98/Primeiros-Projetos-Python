import random

number = random.randint(0, 10)

number_user = int(input('Insira um número de 0 a 100:'))

def adivinha(number, number_user): 
    while number_user != number: 
        number_user = int(input('Errado. Insira um novo número de 0 a 100:'))

    print('Você acertou')

adivinha(number, number_user)