"""Módulo da classe base Produto."""

import math


class Produto:
    """Representa um item genérico do cardápio da lanchonete."""

    def __init__(self, codigo, nome, preco):
        """Cria o produto usando os setters para validar os dados."""
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    @property
    def codigo(self):
        """Retorna o código do produto."""
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        """Define o código, que precisa ser um inteiro positivo."""
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("O código deve ser um número inteiro positivo.")
        self.__codigo = valor

    @property
    def nome(self):
        """Retorna o nome do produto."""
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """Define o nome, impedindo texto vazio."""
        if not valor or not valor.strip():
            raise ValueError("O nome não pode ficar vazio.")
        self.__nome = valor.strip()

    @property
    def preco(self):
        """Retorna o preço base do produto."""
        return self.__preco

    @preco.setter
    def preco(self, valor):
        """Define o preço, que precisa ser um número maior que zero."""
        if not math.isfinite(valor) or valor <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        self.__preco = valor

    @staticmethod
    def formatar_moeda(valor):
        """Converte um número para o formato de moeda brasileira."""
        texto = f"{valor:,.2f}".replace(",", "X")
        return "R$ " + texto.replace(".", ",").replace("X", ".")

    def calcular_preco_final(self):
        """Retorna o preço de venda; cada classe filha sobrescreve a regra."""
        return self.preco

    def __str__(self):
        """Retorna os dados comuns do produto em formato legível."""
        preco = Produto.formatar_moeda(self.preco)
        return f"[{self.codigo:03d}] {self.nome} | Preço base: {preco}"
