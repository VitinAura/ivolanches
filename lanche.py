from produto import Produto


class Lanche(Produto):
    """Classe que representa um lanche do cardápio."""

    def __init__(self, nome: str, preco: float, artesanal: bool):
        """Inicializa um lanche indicando se é artesanal."""
        super().__init__(nome, preco)
        self.artesanal = artesanal

    @property
    def artesanal(self) -> bool:
        """Retorna True se o lanche for artesanal."""
        return self.__artesanal

    @artesanal.setter
    def artesanal(self, valor: bool):
        """Define se o lanche é artesanal."""
        self.__artesanal = bool(valor)

    def adicionar_combo(self) -> float:
        """Método próprio: calcula o valor do lanche com batata e refrigerante (+ R$ 12.00)."""
        return self.preco + 12.00

    def calcular_tempo_preparo(self) -> int:
        """Sobrescreve o tempo de preparo: lanches artesanais levam 20 min, tradicionais 12 min."""
        return 20 if self.artesanal else 12

    def __str__(self) -> str:
        """Retorna os detalhes formatados do lanche."""
        tipo = "Artesanal" if self.artesanal else "Tradicional"
        return f"[Lanche] {super().__str__()} | Tipo: {tipo} | Preparo: {self.calcular_tempo_preparo()} min"
