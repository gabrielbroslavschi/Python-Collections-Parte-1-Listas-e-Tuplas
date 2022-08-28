import array as arr
import numpy as np
from abc import ABCMeta, abstractmethod
from operator import attrgetter
from functools import total_ordering

@total_ordering
class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return 'Codigo {} / Saldo {}'.format(self._codigo, self._saldo)

    def passa_o_mes(self):
        self._saldo -= 2

    @abstractmethod
    def passa_o_mes(self):
        pass


class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass


class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return  self._codigo < outro._codigo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return 'Codigo {}  /  Saldo {}'.format(self._codigo, self._saldo)

class ContaMultiploSalario(ContaSalario):
    pass

#print(Conta(88))

conta16 = ContaCorrente(16)
conta16.deposita(1000)
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
print(conta17)

contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes()
    print(conta)


""" #IREMOS EVITAR DE USAR ARRAY
arrayT = arr.array('d', [1, 3.5])
print(arrayT)"""

#é melhor usar o Numpy para ARRAY
numero = np.array([1, 3.5])
print(numero)
numero += 4
print(numero)




conta1 = ContaSalario(37)
print(conta1)

conta2 = ContaSalario(37)
print(conta2)

print(conta1 == conta2)

print(conta1 in [conta2])
print(conta2 in [conta1])

print(isinstance(ContaCorrente(34), ContaSalario))


idades = [15, 57, 65, 32, 56, 32, 49, 37]

for i in range(len(idades)):
    print(i + 1, idades[i])


enumerate(idades)

print(list(range(len(idades))))

print(list(enumerate(idades)))

for indice, idade in enumerate(idades):
    print(indice, '->',  idade)



usuarios = {
    ('guilherme', 37, 1981),
    ("Daniela", 31,  1987),
    ("Paulo", 39, 1979)
}

for nome, _, _ in usuarios:
    print(nome)


print(sorted(idades))
print(sorted(idades, reverse=True))
print(list(reversed(sorted(idades))))




nomes = ['Guilherme', 'Daniela', 'Paulo']
print(sorted(nomes))

nomes = ['guilherme', 'Daniela', 'Paulo']
print(sorted(nomes))

contaGui = ContaSalario(17)
contaGui.deposita(500)

contaDani = ContaSalario(3)
contaDani.deposita(1000)

contaPaul = ContaSalario(133)
contaPaul.deposita(510)

contas = [contaGui, contaDani, contaPaul]


for conta in sorted(contas):
    print(conta)





contaGuilherme = ContaSalario(17000)
contaGuilherme.deposita(500)

contaDaniela = ContaSalario(3)
contaDaniela.deposita(500)

contaPaulo = ContaSalario(133)
contaPaulo.deposita(500)

contas2 = [contaGuilherme, contaDaniela, contaPaulo]


for conta in sorted(contas2):
    print(conta)