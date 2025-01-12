class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    def __init__(self, clientes, numero, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print(f"CC Número: {self.numero} Saldo: {self.saldo:10.2f}")
        for cliente in self.clientes:
            print(f'Cliente: {cliente.nome} Telefone: {cliente.telefone}')

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente!")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])
    
    def extrato(self):
        print(f"Extrato CC Nº {self.numero}\n")
        for op in self.operacoes:
            print(f"{op[0]:10s} {op[1]:10.2f}")
        print(f"\n    Saldo: {self.saldo:10.2f}\n")

# Criação dos clientes
cliente1 = Cliente("João da Silva", "777-1234")
cliente2 = Cliente("Maria da Silva", "555-4321")

# Criação da conta com os clientes
conta = Conta([cliente1, cliente2], 1234, 500)

# Exibindo o resumo da conta
conta.resumo()