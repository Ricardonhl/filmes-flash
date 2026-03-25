# filmes-flash
# API de Gerenciamento de Filmes (CRUD)
Este projeto é uma API simples desenvolvida com o framework *Flask* em *Python* para gerenciar uma coleção de filmes.

## Funcionalidades (Endpoints)
A API possui as seguintes rotas configuradas:

| Operação    | Método  | Endpoint     | Descrição                                        |
| :---        | :---    | :---         | :---                                             |
| *Listar*    | GET     | /filmes      | Retorna todos os filmes cadastrados.             |
| *Cadastrar* | POST    | /filmes      | Adiciona um novo filme ao arquivo JSON.          |
| *Atualizar* | PUT     | /filmes/<id> | Atualiza os dados de um filme existente pelo ID. |
| *Excluir*   | DELETE  | /filmes/<id> | Remove um filme da base de dados pelo ID.        |

## Tecnologias Utilizadas
* *Python 3.x*
* *Flask* (Micro-framework web)
* *JSON* (Armazenamento de dados)

## Pré-requisitos

Ter o Visual Studio Code instalado no computador
Você vai precisar ter instalado em sua máquina o "Python"

### Instalação do Flask
No terminal do seu VS Code, execute o comando abaixo para instalar a dependência necessária:

pip install flask
