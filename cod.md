# Sistema de Lanchonete (Delivery)

Protótipo desenvolvido em Python aplicando os pilares da Programação Orientada a Objetos (Encapsulamento, Herança e Polimorfismo) e versionamento colaborativo com Git/GitHub.

## Integrantes do Grupo
- [Nome do Integrante 1]
- [Nome do Integrante 2]
- [Nome do Integrante 3]

## Descrição das Classes
- **`Produto` (`produto.py`)**: Classe base com atributos privados (`__nome`, `__preco`), validações via `@property` e método base `calcular_tempo_preparo()`.
- **`Lanche` (`lanche.py`)**: Subclasse de `Produto` com atributo `__artesanal` e método `adicionar_combo()`.
- **`Bebida` (`bebida.py`)**: Subclasse de `Produto` com atributo `__volume_ml` e método `verificar_tamanho_familia()`.
- **`Sobremesa` (`sobremesa.py`)**: Subclasse de `Produto` com atributo `__gelada` e método `embalar_termicamente()`.
- **`Lanchonete` (`lanchonete.py`)**: Classe gerenciadora que armazena os produtos e executa a simulação polimórfica de tempo de preparo.

## Diagrama de Classes

```text
+-----------------------------------+
|            Lanchonete             |
+-----------------------------------+
| - __nome_fantasia: str            |
| - __cardapio: list[Produto]       |
+-----------------------------------+
| + cadastrar_produto(p: Produto)   |
| + listar_produtos()               |
| + buscar_por_nome(termo: str)     |
| + simular_preparo_geral()         |
+-----------------------------------+
                  | 1..*
                  v
+-----------------------------------+
|              Produto              |
+-----------------------------------+
| - __nome: str                     |
| - __preco: float                  |
+-----------------------------------+
| + calcular_tempo_preparo(): int   |
| + __str__(): str                  |
+-----------------------------------+
         ^                ^                ^
         |                |                |
+----------------+ +----------------+ +--------------------+
|     Lanche     | |     Bebida     | |     Sobremesa      |
+----------------+ +----------------+ +--------------------+
| - __artesanal  | | - __volume_ml  | | - __gelada         |
+----------------+ +----------------+ +--------------------+
| + adicionar_   | | + verificar_   | | + embalar_         |
|   combo()      | |   tamanho_fam()| |   termicamente()   |
+----------------+ +----------------+ +--------------------+