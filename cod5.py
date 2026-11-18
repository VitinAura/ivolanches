from produto import Produto


class Lanchonete:
    """Classe gerenciadora responsável pelo catálogo e pedidos da lanchonete."""

    def __init__(self, nome_fantasia: str):
        """Inicializa a lanchonete com um nome e uma lista vazia de produtos."""
        self.__nome_fantasia = nome_fantasia
        self.__cardapio: list[Produto] = []

    @property
    def nome_fantasia(self) -> str:
        """Retorna o nome da lanchonete."""
        return self.__nome_fantasia

    def cadastrar_produto(self, produto: Produto):
        """Adiciona um objeto Produto (ou subclasse) ao cardápio."""
        self.__cardapio.append(produto)

    def listar_produtos(self) -> list[Produto]:
        """Retorna a lista completa de produtos cadastrados."""
        return self.__cardapio

    def buscar_por_nome(self, termo: str) -> list[Produto]:
        """Busca produtos que contenham o termo informado no nome."""
        termo_lower = termo.strip().lower()
        return [p for p in self.__cardapio if termo_lower in p.nome.lower()]

    def simular_preparo_geral(self):
        """Ação polimórfica: percorre o cardápio chamando calcular_tempo_preparo() de cada item."""
        if not self.__cardapio:
            print("Nenhum produto cadastrado para simular preparo.")
            return

        print(f"\n--- Tempo de Preparo por Item ({self.nome_fantasia}) ---")
        tempo_total = 0
        for item in self.__cardapio:
            tempo = item.calcular_tempo_preparo()
            tempo_total += tempo
            print(f"• {item.nome} ({type(item).__name__}): {tempo} minutos")
        print(f"Tempo acumulado de todos os itens: {tempo_total} minutos.")

    def __str__(self) -> str:
        """Retorna um resumo da lanchonete."""
        return f"Lanchonete {self.nome_fantasia} - {len(self.__cardapio)} itens no cardápio."