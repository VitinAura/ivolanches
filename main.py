"""Programa principal: menu da lanchonete no terminal."""

from bebida import Bebida
from lanche import Lanche
from lanchonete import Lanchonete
from produto import Produto
from sobremesa import Sobremesa


def ler_inteiro(mensagem):
    """Pede um número inteiro até o usuário digitar um valor válido."""
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Digite um número inteiro.")


def ler_preco(mensagem):
    """Pede um número decimal, aceitando vírgula ou ponto."""
    while True:
        try:
            return float(input(mensagem).strip().replace(",", "."))
        except ValueError:
            print("Digite um valor numérico. Exemplo: 19,90")


def ler_sim_nao(mensagem):
    """Pede uma resposta de sim ou não e retorna True ou False."""
    while True:
        resposta = input(f"{mensagem} (s/n): ").strip().lower()
        if resposta in ("s", "sim"):
            return True
        if resposta in ("n", "nao", "não"):
            return False
        print("Responda com s ou n.")


def carregar_exemplos(lanchonete):
    """Cadastra um produto de cada tipo para facilitar a demonstração."""
    x_burger = Lanche(1, "X-Burger", 18.90)
    x_burger.adicionar_extra()
    x_burger.adicionar_extra()
    refrigerante = Bebida(2, "Refrigerante", 7.00, 600)
    pudim = Sobremesa(3, "Pudim", 10.00)
    pudim.aplicar_promocao()
    for produto in (x_burger, refrigerante, pudim):
        lanchonete.cadastrar(produto)


def criar_produto(tipo, codigo):
    """Lê os dados do tipo escolhido e cria o objeto correspondente."""
    nome = input("Nome: ")
    preco = ler_preco("Preço base: R$ ")
    if tipo == 1:
        adicionais = ler_inteiro("Quantidade de adicionais: ")
        return Lanche(codigo, nome, preco, adicionais)
    if tipo == 2:
        volume = ler_inteiro("Volume em ml: ")
        gelada = ler_sim_nao("Entregar gelada?")
        return Bebida(codigo, nome, preco, volume, gelada)
    em_promocao = ler_sim_nao("Está em promoção?")
    return Sobremesa(codigo, nome, preco, em_promocao)


def cadastrar_produto(lanchonete):
    """Conduz o cadastro e mostra o erro caso algum dado seja inválido."""
    print("\n--- CADASTRAR PRODUTO ---")
    print("1 - Lanche\n2 - Bebida\n3 - Sobremesa")
    tipo = ler_inteiro("Tipo: ")
    if tipo not in (1, 2, 3):
        print("Tipo inválido.")
        return
    try:
        produto = criar_produto(tipo, lanchonete.proximo_codigo())
        lanchonete.cadastrar(produto)
        print(f"Cadastrado com sucesso: {produto}")
    except ValueError as erro:
        print(f"Não foi possível cadastrar: {erro}")


def listar_produtos(lanchonete):
    """Exibe todos os produtos do cardápio."""
    print(f"\n--- CARDÁPIO: {lanchonete} ---")
    produtos = lanchonete.listar()
    if not produtos:
        print("Nenhum produto cadastrado.")
    for produto in produtos:
        print(produto)


def buscar_produto(lanchonete):
    """Busca produtos pelo código ou por parte do nome."""
    print("\n--- BUSCAR PRODUTO ---")
    termo = input("Digite o código ou o nome: ").strip()
    if not termo:
        print("A busca não pode ficar vazia.")
        return
    if termo.isdecimal():
        produto = lanchonete.buscar_por_codigo(int(termo))
        encontrados = [produto] if produto else []
    else:
        encontrados = lanchonete.buscar_por_nome(termo)
    if not encontrados:
        print("Nenhum produto encontrado.")
    for produto in encontrados:
        print(produto)


def mostrar_precos_finais(lanchonete):
    """Executa a ação polimórfica e mostra o preço final de cada produto."""
    print("\n--- PREÇOS FINAIS (POLIMORFISMO) ---")
    resultados = lanchonete.calcular_precos_finais()
    if not resultados:
        print("Nenhum produto cadastrado.")
    for produto, preco_final in resultados:
        tipo = type(produto).__name__
        valor = Produto.formatar_moeda(preco_final)
        print(f"{tipo:<10} {produto.nome:<25} {valor:>12}")


def exibir_menu():
    """Mostra as opções disponíveis."""
    print("\n========= LANCHONETE DELIVERY =========")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Calcular preços finais")
    print("0 - Sair")


def main():
    """Mantém o menu em execução até o usuário escolher sair."""
    lanchonete = Lanchonete("Lanchonete do Grupo 10")
    carregar_exemplos(lanchonete)
    acoes = {
        1: cadastrar_produto,
        2: listar_produtos,
        3: buscar_produto,
        4: mostrar_precos_finais,
    }
    while True:
        exibir_menu()
        opcao = ler_inteiro("Escolha uma opção: ")
        if opcao == 0:
            print("Sistema encerrado. Até logo!")
            break
        acao = acoes.get(opcao)
        if acao is None:
            print("Opção inválida.")
        else:
            acao(lanchonete)


if __name__ == "__main__":
    main()
