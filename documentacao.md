# Coleção de Endpoints - API de Filmes

Saiba como testar as funcionalidades rotas disponíveis na API.

## 1. Listar Filmes (Read)
Retorna todos os filmes cadastrados no arquivo JSON.
* *URL:* http://127.0.0.1:5000/filmes
* *Método:* GET
* *Sucesso:* Código 200 OK

## 2. Cadastrar Filme (Create)
Adiciona um novo filme à base de dados.
* *URL:* http://127.0.0.1:5000/filmes
* *Método:* POST
* *Corpo (JSON): de exemplo para cadastrar o terceiro filme:* json
  {
    "titulo": "Batman",
    "diretor": "Matt Reeves",
    "ano": 2022
  }