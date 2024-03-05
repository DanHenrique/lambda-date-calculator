# lambda-date-calculator

## Feature

Crie uma pipeline github actions para uma função lambda em python que siga as seguintes regras:

1. Se houver algum commit realizado em branches que se iniciam com "feature/" ou "feature-", serão executados o build da função e também os testes unitarios.
2. Se houver sucesso no build e testes unitarios, sera aberto um Pull Request automaticamente para a branch develop

Separe o build da abertura de Pull Request.
O diretório raiz(root directory) dos testes deve ser parametrizado em um arquivo config.yml na raiz do repositório
O arquivo que será utilizado para dependencias dos testes, requirements, deve ser parametrizado no config.yml

## Develop



## Release

## Main

# E commerce

crie uma tabela dynamo para um ecommerce onde as consultas de produtos serão realizadas por:
- Nome do produto: O usuário pode não saber o nome do produto completo, talvez um contains ou algum algoritmo de busca?
- Categoria
- Subcategoria
- Marca

A tabela deve aceitar ordenação por Nome e por Preço do produto

Pensei nestes campos abaixo

Nome
Descrição
SKU
Peso
Status
    - Desabilitado
    - Habilitado
Dados para frete
    - Altura
    - Largura
    - Comprimento
Flag para destaque
Data de criação
Data de atualização
Cor
Capacidade
Metragem
Marca
Voltagem
Tamanho
Flag Frete Gratis
Flag Black Friday
Preço
Custo
Flag Promoção
Data inicial promoção
Data final promoção
Preço Promocional
Imagens

Meta
    - Title
    - Description
    - Keywords (Tags)
    - Robots ()

Controle de Estoque
    -











Tabela de Produtos:

Campos: ID, Nome, Descrição, SKU, Marca, Peso, Status, Dados para frete, Flag para destaque, Data de criação, Data de atualização, Cor, Imagens
Índices Globais Secundários: NomeIndex (para consultas por nome do produto), MarcaIndex (para consultas por marca), PrecoIndex (para ordenação por preço)
Tabela de Detalhes do Produto:

Campos: ID (chave estrangeira para a tabela de Produtos), Capacidade, Metragem, Voltagem, Tamanho, Flag Frete Grátis, Flag Black Friday, Preço, Custo, Flag Promoção, Data inicial promoção, Data final promoção, Preço Promocional
Índice Global Secundário: IDIndex (para consultar detalhes do produto por ID)
Tabela de Categorias:

Campos: ID, Nome da Categoria
Índice Global Secundário: NomeCategoriaIndex (para consultas por nome da categoria)
Tabela de Subcategorias:

Campos: ID, Nome da Subcategoria, CategoriaID (chave estrangeira para a tabela de Categorias)
Índice Global Secundário: NomeSubcategoriaIndex (para consultas por nome da subcategoria)