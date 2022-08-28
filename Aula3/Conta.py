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