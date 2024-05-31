import time
from datetime import datetime
from prettytable import PrettyTable 

class ContaBancaria:
    LIMITE_SAQUES = 3

    def __init__(self, saldo=0, limite=500):
        self.saldo = saldo
        self.limite = limite
        self.numero_saques = 0
        self.extrato = PrettyTable(["Data", "Historico", "Valor (R$)"])

    def print_extrato(self):
        print("\n================ EXTRATO ================")
        print(f"DISPONIVEL\n\t=Total Disponivel\t {self.saldo}\nÚltimos lançamentos Conta Fácil(C/C + Poupança)")
        print(self.extrato)

    def get_error(self, valor):
        prefixo = 'Operação falhou!'
        erro = {'has_error': False, 'mensagem_erro': ''}
        
        dict_erros = {
            1: '' if self.saldo >= valor else 'Saldo insuficiente.',
            2: '' if self.numero_saques < self.LIMITE_SAQUES else 'Número máximo de saques atingido.',
            3: '' if valor > 0 else 'O valor do saque deve ser superior a zero.',
            4: '' if self.limite >= valor else 'O valor do saque excede o limite permitido.'
        }
        
        mensagens_erro = [msg for msg in dict_erros.values() if msg]
        
        if mensagens_erro:
            if len(mensagens_erro) > 1:
                erro['mensagem_erro'] = f'{prefixo}\n' + '\n'.join(f' - {mensagem}' for mensagem in mensagens_erro)
            else:
                erro['mensagem_erro'] = f'{prefixo} {mensagens_erro[0]}'
            
            erro['has_error'] = True

        return erro

    def saque(self, valor):
        error = self.get_error(valor)
        if error['has_error']:
            print(error['mensagem_erro'])
            return
        
        self.saldo -= valor
        print("Saque realizado com sucesso")
        self.extrato.add_row([datetime.now().strftime("%x"), "Sacar", f"-{valor}"]) 
        self.numero_saques += 1

    def depositar(self, valor):
        if valor <= 0:
            print("Valor deve ser maior que R$0")
            return
            
        self.saldo += valor
        self.extrato.add_row([datetime.now().strftime("%x"), "Depositar", f"{valor}"]) 
        print(f'R${valor} Depositado com sucesso')

class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.conta = ContaBancaria()

    def __str__(self):
        return f'Usuário: {self.nome}, CPF: {self.cpf}'

def cadastrar_usuario(usuarios):
    nome = input("Informe o nome do usuário: ")
    cpf = input("Informe o CPF do usuário: ")
    usuario = Usuario(nome, cpf)
    usuarios.append(usuario)
    print(f'Usuário {nome} cadastrado com sucesso!')

def selecionar_usuario(usuarios):
    cpf = input("Informe o CPF do usuário: ")
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    print("Usuário não encontrado.")
    return None

def main():
    usuarios = []
    menu_principal = """
    
    [c] Cadastrar Usuário
    [l] Logar em Conta
    [q] Sair
    
    => """

    menu_conta = """
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [v] Voltar
    
    => """

    while True:
        opcao = input(menu_principal)

        if opcao == "c":
            cadastrar_usuario(usuarios)

        elif opcao == "l":
            usuario = selecionar_usuario(usuarios)
            if usuario:
                while True:
                    opcao_conta = input(menu_conta)

                    if opcao_conta == "d":
                        valor = int(input('Informe o valor de deposito: '))
                        time.sleep(.3)
                        usuario.conta.depositar(valor)

                    elif opcao_conta == "s":
                        valor = int(input('Informe o valor do saque: '))
                        time.sleep(.3)
                        usuario.conta.saque(valor)

                    elif opcao_conta == "e":
                        usuario.conta.print_extrato()
                        time.sleep(.3)

                    elif opcao_conta == "v":
                        break

                    else:
                        print("Operação inválida, por favor selecione novamente a operação desejada.")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
