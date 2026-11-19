from abc import ABC, abstractmethod

from cliente import Cliente

class Conta(ABC):
    """Classe abstrata que representa uma conta bancária."""

    def __init__(self, numero, cliente, saldo=0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("Número da conta inválido.")
        self._numero = valor

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, valor):
        if not isinstance(valor, Cliente):
            raise TypeError("É necessário informar um Cliente.")
        self._cliente = valor

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("Saldo não pode ser negativo.")
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("O depósito deve ser positivo.")
        self.saldo += valor

    def sacar(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("Valor de saque inválido.")

        if valor > self.saldo:
            raise ValueError("Saldo insuficiente.")

        self.saldo -= valor

    @abstractmethod
    def calcular_rendimento(self):
        """Calcula o rendimento específico da conta."""
        pass

    def __str__(self):
        return (
            f"Conta: {self.numero} | "
            f"Cliente: {self.cliente.nome} | "
            f"Saldo: R$ {self.saldo:.2f}"
        )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.numero}, {self.cliente!r})"

    def __eq__(self, outro):
        if not isinstance(outro, Conta):
            return NotImplemented
        return self.numero == outro.numero
