class Produto:

    def __init__(self, nome: str, preco: float, tempo_preparo: int):
        self.__nome = nome
        self.__preco = preco
        self.__tempo_preparo = tempo_preparo

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, novo_nome: str):
        if not novo_nome or not novo_nome.strip():
            raise ValueError("O nome do produto não pode ser vazio.")
        self.__nome = novo_nome.strip()

    @property
    def preco(self) -> float:
        return self.__preco

    @preco.setter
    def preco(self, novo_preco: float):
        if novo_preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        self.__preco = novo_preco

    @property
    def tempo_preparo(self) -> int:
        return self.__tempo_preparo

    @tempo_preparo.setter
    def tempo_preparo(self, novo_tempo: int):
        if novo_tempo < 0:
            raise ValueError("O tempo de preparo não pode ser negativo.")
        self.__tempo_preparo = novo_tempo

    def calcular_total(self, quantidade: int) -> float:
        return self.__preco * quantidade

    def __str__(self) -> str:
        return f"Produto: {self.__nome} | Preço: R$ {self.__preco:.2f} | Preparo: {self.__tempo_preparo} min"


class Lanche(Produto):

    def __init__(self, nome: str, preco: float, tempo_preparo: int, tamanho: str):
        super().__init__(nome, preco, tempo_preparo)
        self.__tamanho = tamanho

    @property
    def tamanho(self) -> str:
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, novo_tamanho: str):
        if not novo_tamanho or not novo_tamanho.strip():
            raise ValueError("O tamanho não pode ser vazio.")
        self.__tamanho = novo_tamanho.strip()

    def calcular_total(self, quantidade: int) -> float:
        total_base = super().calcular_total(quantidade)
        if self.__tamanho.lower() == "grande":
            total_base += 5.0 * quantidade
        return total_base

    def adicionar_bacon(self) -> str:
        return f"Adicionado bacon extra no lanche {self.nome}!"

    def __str__(self) -> str:
        return f"[Lanche] {super().__str__()} | Tamanho: {self.__tamanho}"


class Bebida(Produto):

    def __init__(self, nome: str, preco: float, tempo_preparo: int, ml: int):
        super().__init__(nome, preco, tempo_preparo)
        self.__ml = ml

    @property
    def ml(self) -> int:
        return self.__ml

    @ml.setter
    def ml(self, novo_ml: int):
        if novo_ml <= 0:
            raise ValueError("A quantidade em ml deve ser maior que zero.")
        self.__ml = novo_ml

    def calcular_total(self, quantidade: int) -> float:
        return super().calcular_total(quantidade)

    def adicionar_gelo_limao(self) -> str:
        return f"Adicionado gelo e limão na bebida {self.nome}!"

    def __str__(self) -> str:
        return f"[Bebida] {super().__str__()} | Volume: {self.__ml}ml"


class Sobremesa(Produto):

    def __init__(self, nome: str, preco: float, tempo_preparo: int, contem_gluten: bool):
        super().__init__(nome, preco, tempo_preparo)
        self.__contem_gluten = contem_gluten

    @property
    def contem_gluten(self) -> bool:
        return self.__contem_gluten

    @contem_gluten.setter
    def contem_gluten(self, status: bool):
        if not isinstance(status, bool):
            raise ValueError("O status de glúten deve ser verdadeiro ou falso (bool).")
        self.__contem_gluten = status

    def calcular_total(self, quantidade: int) -> float:
        total_base = super().calcular_total(quantidade)
        if not self.__contem_gluten:
            total_base += 3.0 * quantidade
        return total_base

    def embalagem_presente(self) -> str:
        return f"A sobremesa {self.nome} foi preparada com embalagem especial para presente!"

    def __str__(self) -> str:
        gluten_str = "Sim" if self.__contem_gluten else "Não (Zero Glúten)"
        return f"[Sobremesa] {super().__str__()} | Contém Glúten: {gluten_str}"


class Lanchonete:

    def __init__(self, nome_lanchonete: str):
        self.__nome_lanchonete = nome_lanchonete
        self.__cardapio = []

    @property
    def nome_lanchonete(self) -> str:
        return self.__nome_lanchonete

    def cadastrar_produto(self, produto: Produto):
        self.__cardapio.append(produto)

    def listar_cardapio(self):
        if not self.__cardapio:
            print("\nNenhum produto cadastrado no cardápio até o momento.")
            return
        print(f"\n--- Cardápio da {self.__nome_lanchonete} ---")
        for i, produto in enumerate(self.__cardapio, 1):
            print(f"{i}. {produto}")

    def buscar_produto(self, nome: str) -> Produto:
        for produto in self.__cardapio:
            if produto.nome.lower() == nome.lower():
                return produto
        return None

    def calcular_pedido_total(self):
        if not self.__cardapio:
            print("\nCardápio vazio.")
            return
        print(f"\n--- Simulação de Cálculo de Itens ({self.__nome_lanchonete}) ---")
        for produto in self.__cardapio:
            total = produto.calcular_total(2)
            print(f"2 unidades de {produto.nome} custam no total: R$ {total:.2f}")


def exibir_menu():
    print("\n========================================")
    print("        LANCHONETE DELIVERY - SISTEMA   ")
    print("========================================")
    print("1. Cadastrar Produto")
    print("2. Listar Cardápio")
    print("3. Buscar Produto por Nome")
    print("4. Simular Cálculo de Pedido (Polimorfismo)")
    print("5. Sair")
    print("========================================")


def main():
    lanchonete = Lanchonete("Burger & Delícias Delivery")

    try:
        lanchonete.cadastrar_produto(Lanche("X-Burger Especial", 25.0, 15, "Grande"))
        lanchonete.cadastrar_produto(Bebida("Refrigerant Cola 350ml", 6.0, 2, 350))
        lanchonete.cadastrar_produto(Sobremesa("Pudim de Leite", 10.0, 5, True))
    except ValueError as e:
        print(f"Erro ao cadastrar dados iniciais: {e}")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ").strip()

        if opcao == "1":
            print("\n--- Cadastro de Novo Produto ---")
            print("Tipos disponíveis: 1 - Lanche | 2 - Bebida | 3 - Sobremesa")
            tipo = input("Escolha o tipo de produto (1/2/3): ").strip()

            if tipo not in ["1", "2", "3"]:
                print("❌ Opção de tipo inválida!")
                continue

            nome = input("Digite o nome do produto: ").strip()
            try:
                preco = float(input("Digite o preço do produto (R$): "))
                tempo_preparo = int(input("Digite o tempo de preparo (min): "))

                if tipo == "1":
                    tamanho = input("Digite o tamanho (ex: P, M, G, Grande): ").strip()
                    novo_produto = Lanche(nome, preco, tempo_preparo, tamanho)
                elif tipo == "2":
                    ml = int(input("Digite o volume em ml: "))
                    novo_produto = Bebida(nome, preco, tempo_preparo, ml)
                else:
                    gluten_input = input("Contém glúten? (s/n): ").strip().lower()
                    contem_gluten = True if gluten_input == 's' else False
                    novo_produto = Sobremesa(nome, preco, tempo_preparo, contem_gluten)

                lanchonete.cadastrar_produto(novo_produto)
                print(f"✅ Produto '{nome}' cadastrado com sucesso!")

            except ValueError as e:
                print(f"❌ Erro de validação ou formato numérico: {e}")

        elif opcao == "2":
            lanchonete.listar_cardapio()

        elif opcao == "3":
            nome_busca = input("\nDigite o nome do produto que deseja buscar: ").strip()
            produto_encontrado = lanchonete.buscar_produto(nome_busca)
            if produto_encontrado:
                print(f"\n🔍 Produto encontrado:\n{produto_encontrado}")
                if isinstance(produto_encontrado, Lanche):
                    print(produto_encontrado.adicionar_bacon())
                elif isinstance(produto_encontrado, Bebida):
                    print(produto_encontrado.adicionar_gelo_limao())
                elif isinstance(produto_encontrado, Sobremesa):
                    print(produto_encontrado.embalagem_presente())
            else:
                print(f"❌ Nenhum produto com o nome '{nome_busca}' foi encontrado.")

        elif opcao == "4":
            lanchonete.calcular_pedido_total()

        elif opcao == "5":
            print("\nEncerrando o sistema. Obrigado por utilizar o software da Lanchonete!")
            break
        else:
            print("❌ Opção inválida! Escolha um número entre 1 e 5.")


if __name__ == "__main__":
    main()
    