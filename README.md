# lambda-date-calculator

## Feature

Crie uma pipeline github actions para uma função lambda em python que siga as seguintes regras:

1. Se houver algum commit realizado em branches que se iniciam com "feature/" ou "feature-", serão executados o build da função e também os testes unitarios.
2. Se houver sucesso no build e testes unitarios, sera aberto um Pull Request automaticamente para a branch develop

Separe o build da abertura de Pull Request.
O diretório raiz(root directory) dos testes deve ser parametrizado em um arquivo config.yml na raiz do repositório
O arquivo que será utilizado para dependencias dos testes, requirements, deve ser parametrizado no config.yml

## Develop

