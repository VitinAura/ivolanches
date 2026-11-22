"""Módulo da classe Sobremesa."""

from produto import Produto


class Sobremesa(Produto):
    """Representa uma sobremesa, que pode estar em promoção."""

    DESCONTO_PROMOCAO = 0.10

    def __init__(self, codigo, nome, preco, em_promocao=False):
        """Cria a sobremesa aproveitando o construtor de Produto."""
        super().__init__(codigo, nome, preco)
        self.em_promocao = em_promocao

    @property
    def em_promocao(self):
        """Informa se a sobremesa está em promoção."""
        return self.__em_promocao

    @em_promocao.setter
    def em_promocao(self, valor):
        """Define se a sobremesa está em promoção."""
        self.__em_promocao = bool(valor)

    def aplicar_promocao(self):
        """Coloca a sobremesa em promoção."""
        self.em_promocao = True

    def calcular_preco_final(self):
        """Aplica 10% de desconto quando a sobremesa está em promoção."""
        if self.em_promocao:
            return round(self.preco * (1 - Sobremesa.DESCONTO_PROMOCAO), 2)
        return self.preco

    def __str__(self):
        """Retorna os dados da sobremesa em formato legível."""
        promocao = "em promoção" if self.em_promocao else "sem promoção"
        return f"Sobremesa {super().__str__()} | {promocao}"
