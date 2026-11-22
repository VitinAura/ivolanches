"""Módulo da classe Bebida."""

from produto import Produto


class Bebida(Produto):
    """Representa uma bebida, que pode ser entregue gelada."""

    TAXA_GELADA = 1.00

    def __init__(self, codigo, nome, preco, volume_ml, gelada=True):
        """Cria a bebida aproveitando o construtor de Produto."""
        super().__init__(codigo, nome, preco)
        self.volume_ml = volume_ml
        self.gelada = gelada

    @property
    def volume_ml(self):
        """Retorna o volume da bebida em mililitros."""
        return self.__volume_ml

    @volume_ml.setter
    def volume_ml(self, valor):
        """Define o volume, que precisa ser maior que zero."""
        if valor <= 0:
            raise ValueError("O volume deve ser maior que zero.")
        self.__volume_ml = valor

    @property
    def gelada(self):
        """Informa se a bebida será entregue gelada."""
        return self.__gelada

    @gelada.setter
    def gelada(self, valor):
        """Define se a bebida será entregue gelada."""
        self.__gelada = bool(valor)

    def volume_em_litros(self):
        """Converte o volume de mililitros para litros."""
        return self.volume_ml / 1000

    def calcular_preco_final(self):
        """Cobra a taxa de refrigeração quando a bebida é gelada."""
        if self.gelada:
            return self.preco + Bebida.TAXA_GELADA
        return self.preco

    def __str__(self):
        """Retorna os dados da bebida em formato legível."""
        estado = "gelada" if self.gelada else "natural"
        litros = f"{self.volume_em_litros():.2f}".replace(".", ",")
        return f"Bebida {super().__str__()} | {litros} L | {estado}"
