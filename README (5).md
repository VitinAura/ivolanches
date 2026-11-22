# Sistema de Lanchonete Delivery

Protótipo em Python, executado no terminal, para organizar o cardápio de uma lanchonete com Programação Orientada a Objetos.

**Tema:** Lanchonete (delivery)

## Integrantes

- Victor Caglioni
- Otavio
- Isaac

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
