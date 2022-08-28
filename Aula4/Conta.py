import array as arr
import numpy as np
from abc import ABCMeta, abstractmethod

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