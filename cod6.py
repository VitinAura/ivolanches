from lanchonete import Lanchonete
from lanche import Lanche
from bebida import Bebida
from sobremesa import Sobremesa


def exibir_menu():
    """Exibe as opções do sistema no terminal."""
    print("\n" + "=" * 40)
    print("   SISTEMA DE DELIVERY - LANCHONETE")
    print("=" * 40)
    print("1. Cadastrar produto")
    print("2. Listar cardápio")
    print("3. Buscar produto por nome")
    print("4. Calcular tempo de preparo (Polimorfismo)")
    print("5. Sair")
    print("=" * 40)


def cadastrar_item(sistema: Lanchonete):
    """Coleta dados do usuário e instancia a classe filha correspondente."""
    print("\nTipo de produto: [1] Lanche | [2] Bebida | [3] Sobremesa")
    tipo = input("Escolha o tipo: ").strip()

    try:
        nome = input("Nome do produto: ")
        preco = float(input("Preço (R$): ").replace(",", "."))

        if tipo == "1":
            art = input("É artesanal? (s/n): ").strip().lower() == "s"
            produto = Lanche(nome, preco, art)
            sistema.cadastrar_produto(produto)
            print(f"Lanche cadastrado! Valor no combo: R$ {produto.adicionar_combo():.2f}")

        elif tipo == "2":
            volume = int(input("Volume (em ml): "))
            produto = Bebida(nome, preco, volume)
            sistema.cadastrar_produto(produto)
            print("Bebida cadastrada com sucesso!")

        elif tipo == "3":
            gelada = input("É servida gelada? (s/n): ").strip().lower() == "s"
            produto = Sobremesa(nome, preco, gelada)
            sistema.cadastrar_produto(produto)
            print(f"Sobremesa cadastrada! ({produto.embalar_termicamente()})")

        else:
            print("Tipo de produto inválido.")

    except ValueError as erro:
        print(f"Erro de validação: {erro}")


def main():
    """Função principal que executa o loop do menu."""
    sistema = Lanchonete("Sabor Express Delivery")

    # Itens iniciais para facilitar testes e demonstração
    sistema.cadastrar_produto(Lanche("X-Bacon Artesanal", 32.00, True))
    sistema.cadastrar_produto(Bebida("Refrigerante 2L", 12.00, 2000))
    sistema.cadastrar_produto(Sobremesa("Pudim de Leite", 9.50, True))

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_item(sistema)

        elif opcao == "2":
            produtos = sistema.listar_produtos()
            print(f"\n--- Cardápio ({len(produtos)} itens) ---")
            for p in produtos:
                print(p)

        elif opcao == "3":
            termo = input("Digite o nome para busca: ")
            encontrados = sistema.buscar_por_nome(termo)
            if encontrados:
                print("\n--- Resultados da Busca ---")
                for p in encontrados:
                    print(p)
            else:
                print("Nenhum produto encontrado com esse nome.")

        elif opcao == "4":
            sistema.simular_preparo_geral()

        elif opcao == "5":
            print("Encerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()