class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)


contaGui = ContaCorrente(15)
print(contaGui)

contaGui.deposita(500)
print(contaGui)


contaDani = ContaCorrente(123123)
contaDani.deposita(1000)
print(contaDani)

contas = [contaGui, contaDani]
print(contas)

for conta in contas:
    print(conta)



"""contas = [contaGui, contaDani, contaGui]
print(contas[0])
contaGui.deposita(100)
print(contas[0])
print(contas[2])"""

def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])


contas.insert(0,76)
print(contas[0], contas[1], contas[2])



"""deposita_para_todas(contas)
print(contas[0], contas[1], contas[2])"""

guilherme = ("Guilherme", 32, 1981)
daniela = ('Daniela', 31, 1987)

usuarios = [guilherme, daniela]
print(usuarios)


usuarios.append(('Paulo', 39, 1979))
print(usuarios)