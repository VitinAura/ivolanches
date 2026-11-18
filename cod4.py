from produto import Produto


class Sobremesa(Produto):
    """Classe que representa uma sobremesa do cardápio."""

    def __init__(self, nome: str, preco: float, gelada: bool):
        """Inicializa uma sobremesa indicando se é servida gelada."""
        super().__init__(nome, preco)
        self.gelada = gelada

    @property
    def gelada(self) -> bool:
        """Retorna True se a sobremesa for gelada."""
        return self.__gelada

    @gelada.setter
    def gelada(self, valor: bool):
        """Define se a sobremesa é gelada."""
        self.__gelada = bool(valor)

    def embalar_termicamente(self) -> str:
        """Método próprio: define o tipo de embalagem para delivery."""
        return "Embalagem térmica refrigerada" if self.gelada else "Caixa padrão"

    def calcular_tempo_preparo(self) -> int:
        """Sobrescreve o tempo de preparo: sobremesas levam 7 min para montagem."""
        return 7

    def __str__(self) -> str:
        """Retorna os detalhes formatados da sobremesa."""
        temp = "Gelada" if self.gelada else "Ambiente"
        return f"[Sobremesa] {super().__str__()} | Temp: {temp} | Preparo: {self.calcular_tempo_preparo()} min"