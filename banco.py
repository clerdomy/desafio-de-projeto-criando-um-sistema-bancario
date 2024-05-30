
import time
from datetime import datetime
from prettytable import PrettyTable 


saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3
extrato = PrettyTable(["Data", "Historico", "Valor (R$)"])

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


def print_extrato():
    global extrato, saldo
    print("\n================ EXTRATO ================")
    print(f"""DISPONIVEL\n\t=Total Disponivel\t {saldo}
    \nÚltmos lançamentos Conta Fácil(C/C + Poupança)""")
    print(extrato)

def get_error(saldo, valor, limite, numero_saques):
    global LIMITE_SAQUES

    prefixo = 'Operação falhou!'
    erro = {'has_error': False, 'mensagem_erro': ''}
    
    # Dicionário de erros
    dict_erros = {
        1: '' if saldo >= valor else 'Saldo insuficiente.',
        2: '' if numero_saques < LIMITE_SAQUES else 'Número máximo de saques atingido.',
        3: '' if valor > 0 else 'O valor do saque deve ser superior a zero.',
        4: '' if limite >= valor else 'O valor do saque excede o limite permitido.'
    }
    
    # Filtra as mensagens de erro
    mensagens_erro = [msg for msg in dict_erros.values() if msg]
    
    if mensagens_erro:
        if len(mensagens_erro) > 1:
            erro['mensagem_erro'] = f'{prefixo}\n' + '\n'.join(f' - {mensagem}' for mensagem in mensagens_erro)
        else:
            erro['mensagem_erro'] = f'{prefixo} {mensagens_erro[0]}'
        
        erro['has_error'] = True

    return erro

def saque(valor):
    global extrato, saldo, limite, numero_saques
    error = get_error(saldo,  valor, limite, numero_saques)
    if error['has_error']:
        print(error['mensagem_erro'])
        return
    
    saldo-= valor
    print("Saque realizado com sucesso")
    extrato.add_row([datetime.now().strftime("%x"), "Sacar", f"-{valor}"]) 
    numero_saques +=1

def depositar(valor):
    global saldo, extrato

    if valor <= 0:
        print("Valor deve ser maior que R$0")
        return
        
    saldo += valor
    extrato.add_row([datetime.now().strftime("%x"), "Depositar", f"{valor}"]) 
    print(f'R${valor} Depositado com sucesso')


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = int(input('Informe o valor de deposito: '))
        time.sleep(.3)
        depositar(valor)



    elif opcao == "s":
        valor = int(input('Informe o valor do saque: '))
        time.sleep(.3)
        saque(valor)

    elif opcao == "e":
        print_extrato()
        time.sleep(.3)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")