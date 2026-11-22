"""Módulo da classe Lanche."""

from produto import Produto


class Lanche(Produto):
    """Representa um lanche, que pode receber adicionais pagos."""

    PRECO_ADICIONAL = 2.50

    def __init__(self, codigo, nome, preco, qtd_adicionais=0):
        """Cria o lanche aproveitando o construtor de Produto."""
        super().__init__(codigo, nome, preco)
        self.qtd_adicionais = qtd_adicionais

    @property
    def qtd_adicionais(self):
        """Retorna a quantidade de adicionais do lanche."""
        return self.__qtd_adicionais

    @qtd_adicionais.setter
    def qtd_adicionais(self, valor):
        """Define os adicionais, impedindo quantidade negativa."""
        if valor < 0:
            raise ValueError("A quantidade de adicionais não pode ser negativa.")
        self.__qtd_adicionais = valor

    def adicionar_extra(self):
        """Acrescenta um adicional ao lanche."""
        self.qtd_adicionais += 1

    def calcular_preco_final(self):
        """Soma ao preço base o valor de cada adicional."""
        return self.preco + self.qtd_adicionais * Lanche.PRECO_ADICIONAL

    def __str__(self):
        """Retorna os dados do lanche em formato legível."""
        return f"Lanche {super().__str__()} | Adicionais: {self.qtd_adicionais}"
