# Sistema de Lanchonete Delivery

Protótipo em Python, executado no terminal, para organizar o cardápio de uma lanchonete com Programação Orientada a Objetos.

**Tema:** Lanchonete (delivery)

## Integrantes

- Victor Caglioni
- Otavio
- Isaac

## Descrição das classes

- **Produto** (`produto.py`): classe base com código, nome e preço privados, validados nos setters.
- **Lanche** (`lanche.py`): herda de Produto e cobra R$ 2,50 por adicional.
- **Bebida** (`bebida.py`): herda de Produto, tem volume e cobra R$ 1,00 quando é gelada.
- **Sobremesa** (`sobremesa.py`): herda de Produto e aplica 10% de desconto em promoção.
- **Lanchonete** (`lanchonete.py`): classe gerenciadora que guarda a lista de produtos.
- **main.py**: menu do terminal para cadastrar, listar, buscar e calcular os preços finais.

## Diagrama de classes

```text
                 +--------------------------------+
                 |            Produto             |
                 +--------------------------------+
                 | - __codigo / __nome / __preco  |
                 +--------------------------------+
                 | + calcular_preco_final()       |
                 | + formatar_moeda()             |
                 | + __str__()                    |
                 +---------------^----------------+
                                 | herda
        +------------------------+-----------------------+
        |                        |                       |
+-------+----------+  +----------+---------+  +----------+---------+
|      Lanche      |  |       Bebida       |  |     Sobremesa      |
+------------------+  +--------------------+  +--------------------+
| - __qtd_adicionais| | - __volume_ml      |  | - __em_promocao    |
|                  |  | - __gelada         |  |                    |
+------------------+  +--------------------+  +--------------------+
| + adicionar_extra|  | + volume_em_litros |  | + aplicar_promocao |
| + calcular_preco_final() (sobrescrito nas três classes)          |
+------------------------------------------------------------------+

+--------------------------------+
|           Lanchonete           |   guarda uma lista de Produto
+--------------------------------+   (1 Lanchonete : N Produtos)
| - __nome / __produtos          |
+--------------------------------+
| + cadastrar() / listar()       |
| + buscar_por_codigo()          |
| + buscar_por_nome()            |
| + calcular_precos_finais()     |
+--------------------------------+
```

## Divisão de arquivos

| Integrante | Responsabilidade |
|---|---|
| Victor Caglioni | `produto.py`, `main.py` e apresentação |
| Otavio | `lanche.py` e `bebida.py` |
| Isaac | `sobremesa.py` e `lanchonete.py` |

## Como executar

1. Instale o Python 3.10 ou superior.
2. Clone o repositório:

```bash
git clone https://github.com/VitinAura/poo-grupo10-lanchonete.git
```

3. Abra a pasta `poo-grupo10-lanchonete` no PyCharm.
4. Clique com o botão direito em `main.py` e escolha **Run 'main'**.

Pelo terminal, dentro da pasta do projeto:

```bash
python main.py
```
