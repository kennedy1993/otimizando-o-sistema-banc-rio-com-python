class ContaBancaria:
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        print(f'Depósito de R${
              valor} realizado com sucesso. Novo saldo: R${self.saldo}')

    def saque(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            print(f'Saque de R${
                  valor} realizado com sucesso. Novo saldo: R${self.saldo}')

    def extrato(self):
        print(f'Saldo atual: R${self.saldo}')


def cadastrar_usuario(nome, cpf):
    return {'nome': nome, 'cpf': cpf}


def cadastrar_conta(usuario):
    return ContaBancaria(usuario)


# Exemplo de uso:
if __name__ == "__main__":
    # Cadastrar usuário
    usuario1 = cadastrar_usuario('João', '123.456.789-00')

    # Cadastrar conta bancária associada ao usuário
    conta1 = cadastrar_conta(usuario1)

    # Realizar operações na conta
    conta1.deposito(1000)
    conta1.saque(500)
    conta1.extrato()
