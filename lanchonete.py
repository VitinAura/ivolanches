"""Módulo da classe gerenciadora Lanchonete."""


class Lanchonete:
    """Guarda e gerencia a lista de produtos do cardápio."""

    def __init__(self, nome):
        """Cria a lanchonete com o cardápio vazio."""
        self.nome = nome
        self.__produtos = []

    @property
    def nome(self):
        """Retorna o nome da lanchonete."""
        return self.__nome

    @nome.setter
    def nome(self, valor):
        """Define o nome da lanchonete, impedindo texto vazio."""
        if not valor or not valor.strip():
            raise ValueError("O nome da lanchonete não pode ficar vazio.")
        self.__nome = valor.strip()

    def proximo_codigo(self):
        """Retorna o próximo código livre do cardápio."""
        return max((p.codigo for p in self.__produtos), default=0) + 1

    def cadastrar(self, produto):
        """Adiciona um produto, impedindo código repetido."""
        if self.buscar_por_codigo(produto.codigo) is not None:
            raise ValueError("Já existe um produto com esse código.")
        self.__produtos.append(produto)

    def listar(self):
        """Retorna uma cópia da lista para proteger o cardápio original."""
        return list(self.__produtos)

    def buscar_por_codigo(self, codigo):
        """Retorna o produto com o código informado ou None."""
        for produto in self.__produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def buscar_por_nome(self, termo):
        """Retorna os produtos cujo nome contém o termo pesquisado."""
        termo = termo.strip().lower()
        return [p for p in self.__produtos if termo in p.nome.lower()]

    def calcular_precos_finais(self):
        """Percorre a lista e chama o método polimórfico de cada produto."""
        resultado = []
        for produto in self.__produtos:
            resultado.append((produto, produto.calcular_preco_final()))
        return resultado

    def __str__(self):
        """Retorna o nome da lanchonete e o total de produtos."""
        return f"{self.nome} ({len(self.__produtos)} produtos no cardápio)"
