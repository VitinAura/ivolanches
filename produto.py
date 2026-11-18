class Produto:
    """Classe base que representa um produto genérico da lanchonete."""

    def __init__(self, nome: str, preco: float):
        """Inicializa um produto com nome e preço validados."""
        self.nome = nome
        self.preco = preco

    @property
    def nome(self) -> str:
        """Retorna o nome do produto."""
        return self.__nome

    @nome.setter
    def nome(self, valor: str):
        """Define o nome do produto, garantindo que não seja vazio."""
        if not valor or not valor.strip():
            raise ValueError("O nome do produto não pode estar vazio.")
        self.__nome = valor.strip()

    @property
    def preco(self) -> float:
        """Retorna o preço do produto."""
        return self.__preco

    @preco.setter
    def preco(self, valor: float):
        """Define o preço do produto, garantindo que seja maior que zero."""
        if valor <= 0:
            raise ValueError("O preço do produto deve ser maior que zero.")
        self.__preco = float(valor)

    def calcular_tempo_preparo(self) -> int:
        """Calcula o tempo base de preparo em minutos (método polimórfico)."""
        return 5

    def __str__(self) -> str:
        """Retorna uma representação legível do produto."""
        return f"{self.nome} - R$ {self.preco:.2f}"
