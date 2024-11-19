from datetime import datetime
saldo = 0.00
contador = 0
extrato = [] # Lista para armazenar transações

print("#Bem Vindo ao Banco Python#")

def menu():
    print(datetime.now().strftime('%d-%m-%Y'))
    print("Selecione a Opção que deseja realizar:")
    opcao = int(input(" [1]Depositar \n [2]Sacar \n [3]Extrato \n"))

    if opcao == 1:
        valor = float(input("Qual valor você deseja depositar? "))
        depositar(valor)
    elif opcao == 2:
        valor = float(input("Qual valor você deseja sacar? "))
        sacar(valor)
    elif opcao == 3:
        mostrar_extrato()
    else:
        print("Opção inválida.")
        return menu()
    #
#

def depositar(valor):
    global saldo
    contador = 0
    if  valor > 0:
        saldo += valor
        print(f"Depósito reali1zado com sucesso! Saldo atual: R$ {saldo:.2f}")

        transacao = {
            'data': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            'tipo': 'Depósito',
            'valor': valor,
            'saldo': saldo
        }
        extrato.append(transacao)  # Adiciona a transação à lista

    else:
        print("Opção inválida.")
    #
    return menu()
#

def sacar(valor):
    global saldo, contador
    if (saldo >= valor and valor < 500 and contador < 3):
        saldo -= valor
        print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
        contador += 1 
        print(f"Você realizou {contador} saque(s) hoje")

        transacao = {
            'data': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            'tipo': 'Saque',
            'valor': valor,
            'saldo': saldo
        }
        extrato.append(transacao)  # Adiciona a transação à lista
    elif valor >= 500:
        print("Valor do Saque não pode ser igual ou superior a R$500,00")
    elif contador >= 3: 
        print ("Você não pode realizar mais de 3 saques por dia")
    else:
        print("Saldo insuficiente!")
    #
    return menu()
#

def mostrar_extrato():
    if not extrato: 
        print ("Nenhuma transação realizada")
    else:
        print("\n #EXTRATO#")
        for transacao in extrato:
            print(f"{transacao['data']} | {transacao['tipo']} | R$ {transacao['valor']:.2f} | Saldo: R$ {transacao['saldo']:.2f}")
    return

menu()
