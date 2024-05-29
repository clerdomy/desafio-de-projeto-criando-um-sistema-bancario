
import time
from datetime import datetime
from prettytable import PrettyTable 

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500

def extrato(saldo, historico):
    extrato = f"""DISPONIVEL
    =Total Disponivel\t {saldo}
    Últmos lançamentos Conta Fácil(C/C + Poupança)
    """
    print(extrato)
    print(historico)

historico = PrettyTable(["Data", "Historico", "Valor (R$)"]) 
 
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = int(input('Informe o valor de deposito: '))
        if valor <= 0:
            print("Valor deve ser maior que R$0")
        
            time.sleep(.8)
            continue
        saldo += valor
        historico.add_row([datetime.now().strftime("%x"), "Depositar", f"{valor}"]) 
        time.sleep(.9)
        print(f'R${valor} Depositado com sucesso')
        time.sleep(.2)

    elif opcao == "s":
        valor = int(input('Informe o valor: '))
        time.sleep(.3)
        if valor <=0:
            print("Operação falhou! Valor deve ser maior que R$0")
        
        elif valor > 500:
            print("Operação falhou! O valor do saque excede o limite.")
            print("Valor deve ser menor ou igual a R$500")

        elif numero_saques > 2 or LIMITE_SAQUES < 1:
            print("Operação falhou! O valor do saque excede o limite. de saque")

        elif saldo < valor:
            print("Operação falhou! Você não tem saldo suficiente.")
        else:
            time.sleep(.2)
            saldo-= valor
            print("Saque realizado com sucesso")
            time.sleep(.2)
            historico.add_row([datetime.now().strftime("%x"), "Sacar", f"-{valor}"]) 
            numero_saques +=1 
            LIMITE_SAQUES -=1

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        extrato(saldo, historico)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")