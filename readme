# Sistema de Banco em Python

Este projeto é um sistema simples de banco em Python, que permite a criação de contas correntes para múltiplos usuários, e oferece funcionalidades básicas como depósito, saque e exibição de extrato.

## Funcionalidades

- Cadastro de usuários com nome e CPF.
- Cada usuário tem uma conta corrente com saldo, limite de saque e um extrato de transações.
- Realização de depósitos e saques.
- Exibição do extrato da conta com histórico de transações.

## Como usar

1. Clone o repositório para sua máquina local.
2. Certifique-se de ter o Python instalado.
3. Instale as dependências necessárias, executando o seguinte comando:
    ```bash
    pip install prettytable
    ```
4. Execute o script `main.py` para iniciar o sistema:
    ```bash
    python main.py
    ```

## Menu Principal

- `[c]` Cadastrar Usuário: Permite cadastrar um novo usuário.
- `[l]` Logar em Conta: Permite logar na conta de um usuário existente usando o CPF.
- `[q]` Sair: Encerra o programa.

## Menu de Conta

- `[d]` Depositar: Permite realizar um depósito na conta logada.
- `[s]` Sacar: Permite realizar um saque na conta logada.
- `[e]` Extrato: Exibe o extrato da conta logada.
- `[v]` Voltar: Retorna ao menu principal.

## Estrutura do Código

### Classe `ContaBancaria`

Representa uma conta bancária com saldo, limite de saque, número de saques e extrato.

#### Métodos

- `print_extrato()`: Exibe o extrato da conta.
- `get_error(valor)`: Verifica se há erros em uma operação de saque.
- `saque(valor)`: Realiza um saque na conta.
- `depositar(valor)`: Realiza um depósito na conta.

### Classe `Usuario`

Representa um usuário do banco com nome, CPF e uma conta bancária.

### Funções

- `cadastrar_usuario(usuarios)`: Cadastra um novo usuário.
- `selecionar_usuario(usuarios)`: Seleciona um usuário existente pelo CPF.
- `main()`: Função principal que gerencia o menu e a interação com o usuário.

## Exemplo de Uso

1. No menu principal, selecione `[c]` para cadastrar um novo usuário.
2. Informe o nome e CPF do usuário.
3. No menu principal, selecione `[l]` para logar na conta do usuário.
4. No menu de conta, selecione `[d]` para depositar, `[s]` para sacar, `[e]` para exibir o extrato, ou `[v]` para voltar ao menu principal.

## Autor

Desenvolvido por clerdomy zidor.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
