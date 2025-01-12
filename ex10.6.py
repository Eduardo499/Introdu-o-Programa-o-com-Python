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


cliente1 = Cliente("João da Silva", "777-1234")
cliente2 = Cliente("Maria da Silva", "555-4321")

conta1 = Conta([cliente1], 1, 1000)
conta2 = Conta([cliente2], 2, 500)

conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta1.saque(250)
conta2.deposito(100)
conta1.deposito(500)
conta2.saque(250)
conta1.deposito(1000)
conta1.saque(10000)
conta2.saque(1000)
conta1.deposito(1000)
conta2.saque(1000)
conta1.deposito(1000)
conta2.saque(1000)
conta1.deposito(1000)
conta2.saque(1000)
conta1.deposito(1000)
conta2.saque(1000)
conta1.deposito(1000)
conta2.saque(1000)
conta1.deposito(1000)
conta1.extrato()
conta2.extrato()