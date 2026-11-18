from produto import Produto


class Bebida(Produto):
    """Classe que representa uma bebida do cardápio."""

    def __init__(self, nome: str, preco: float, volume_ml: int):
        """Inicializa uma bebida com seu volume em mililitros."""
        super().__init__(nome, preco)
        self.volume_ml = volume_ml

    @property
    def volume_ml(self) -> int:
        """Retorna o volume da bebida em ml."""
        return self.__volume_ml

    @volume_ml.setter
    def volume_ml(self, valor: int):
        """Define o volume em ml, exigindo valor positivo."""
        if valor <= 0:
            raise ValueError("O volume da bebida deve ser maior que zero.")
        self.__volume_ml = int(valor)

    def verificar_tamanho_familia(self) -> bool:
        """Método próprio: verifica se a bebida tem 1000ml ou mais."""
        return self.volume_ml >= 1000

    def calcular_tempo_preparo(self) -> int:
        """Sobrescreve o tempo de preparo: bebidas apenas são separadas (2 min)."""
        return 2

    def __str__(self) -> str:
        """Retorna os detalhes formatados da bebida."""
        familia = " (Tamanho Família)" if self.verificar_tamanho_familia() else ""
        return f"[Bebida] {super().__str__()} | Volume: {self.volume_ml}ml{familia} | Preparo: {self.calcular_tempo_preparo()} min"