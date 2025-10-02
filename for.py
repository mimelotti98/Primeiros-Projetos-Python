
def media_final(): 
    media = 0

    for i in range(1,4):
        nota = float(input(f'Informe sua nota {i}: '))

        media = media + nota

    print(media / 3)

media_final()