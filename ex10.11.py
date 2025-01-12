class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def abre_conta(self, conta):
        self.contas.append(conta)

    def lista_contas(self):
        for c in self.contas:
            c.resumo()

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
            return True
        else:
            print("Saldo insuficiente!")
            return False

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])
    
    def extrato(self):
        print(f"Extrato CC Nº {self.numero}\n")
        for op in self.operacoes:
            print(f"{op[0]:10s} {op[1]:10.2f}")
        print(f"\n    Saldo: {self.saldo:10.2f}\n")

class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        super().__init__(clientes, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
            return True
        else:
            print("Saldo insuficiente!")
            return False

    def extrato(self):
        super().extrato()
        print(f"Limite: {self.limite:10.2f}")
        print(f'Total disponível: {self.saldo + self.limite:10.2f}')

# Criação dos clientes
joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")

# Criação das contas
conta1 = Conta([joão], 1, 1000)
conta2 = ContaEspecial([maria, joão], 2, 500, 1000)

# Operações nas contas
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()
conta2.deposito(200)
conta2.extrato()