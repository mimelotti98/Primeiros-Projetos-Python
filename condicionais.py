idade = int(input('Quantos anos você tem?'))
media = float(input('Qual foi sua nota?'))

def verificar_idade(idade):
    if idade >= 18: 
        print('Você é maior de idade')
    else:
        print('Você é menor de idada')

def verificar_media(media):
    if media >= 7: 
        print('Você foi aprovado')
    elif media >= 5: 
        print('Recuperação')
    else:
        print('Você foi reprovado')


verificar_idade(idade)
verificar_media(media)
