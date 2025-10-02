print('########## MENU ##########')
print('Digite o caracter referente a operação desejada:')
print('[+] Soma')
print('[-] Subtração')
print('[*] Multiplicação')
print('[/] Divisão')
escolhida = input('Qual você deseja?')

num1 = float(input('Agora digite o primeiro número:'))

num2 = float(input('Agora digite o segundo número:'))


def operacao (num1, num2, escolhida): 
    if escolhida == "+":
        return num1 + num2
    elif escolhida == "-":
        return num1 - num2
    elif escolhida == "*":
        return num1 * num2
    elif escolhida == "/":
        return num1 / num2
    else:
        print('opção invalida')


resultado = operacao (num1, num2, escolhida)
print(f'O resultado é: {resultado}')