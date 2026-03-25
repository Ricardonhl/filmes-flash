# Documentação dos Endpoints da API

Esta documentação detalha como interagir com a API de Filmes. Todas as requisições devem utilizar o cabeçalho Content-Type: application/json.
---
## 1. Listar Filmes
Retorna a lista completa de filmes armazenados no arquivo JSON.

* *URL:* /filmes
* *Método:* GET
* *Resposta de Sucesso:*
    * *Código:* 200 OK
    * *Conteúdo:* [{"id": 1, "titulo": "Aquaman", "diretor": "James Wan", "ano": 2018},
                   {"id": 2, "titulo": "Transformers", "diretor": "Michael Bay", "ano": 2007}]

---
## 2. Cadastrar Filme
Adiciona um novo filme à base de dados. O ID é gerado automaticamente pelo servidor.

* *URL:* /filmes
* *Método:* POST
* *Corpo da Requisição (JSON):*
    json
    {
      "titulo": "Aquaman",
      "diretor": "James Wan",
      "ano": 2018
    }
    
* *Resposta de Sucesso:*
    * *Código:* 201 CREATED
    * *Conteúdo:* {"id": 3, "titulo": "Interestelar", ...}

---
## 3. Atualizar Filme
Altera os dados de um filme já existente com base no ID fornecido na URL.

* *URL:* /filmes/<id> (Exemplo: /filmes/1)
* *Método:* PUT
* *Corpo da Requisição (JSON):*
    json
    {
        "titulo": "Inception (Edição Especial)",
        "ano": 2011
    }
    
* *Respostas:*
    * *Sucesso (200 OK):* Retorna o objeto atualizado.
    * *Erro (404 NOT FOUND):* Caso o ID não exista.

---
## 4. Excluir Filme
Remove permanentemente um filme da base de dados.

* *URL:* /filmes/<id>
* *Método:* DELETE
* *Respostas:*
    * *Sucesso (200 OK):* {"mensagem": "Filme removido com sucesso"}
    * *Erro (404 NOT FOUND):* {"erro": "Filme não encontrado"}
