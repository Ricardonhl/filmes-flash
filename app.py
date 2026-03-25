from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
NOME_ARQUIVO = 'filmes.json'

def ler_dados():
    if not os.path.exists(NOME_ARQUIVO):
        return []
    with open(NOME_ARQUIVO, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def salvar_dados(dados):
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# 1. Read
@app.route('/filmes', methods=['GET'])
def listar_filmes():
    return jsonify(ler_dados()), 200

# 2. Create
@app.route('/filmes', methods=['POST'])
def cadastrar_filme():
    novo_filme = request.get_json()
    dados = ler_dados()
    
    novo_id = dados[-1]['id'] + 1 if dados else 1
    novo_filme['id'] = novo_id
    
    dados.append(novo_filme)
    salvar_dados(dados)
    return jsonify(novo_filme), 201

# 3. Update
@app.route('/filmes/<int:id>', methods=['PUT'])
def atualizar_filme(id):
    dados = ler_dados()
    filme_atualizado = request.get_json()
    
    for i, filme in enumerate(dados):
        if filme['id'] == id:
            dados[i].update(filme_atualizado)
            dados[i]['id'] = id
            salvar_dados(dados)
            return jsonify(dados[i]), 200         
    return jsonify({"erro": "Filme não encontrado"}), 404

# 4. Delete
@app.route('/filmes/<int:id>', methods=['DELETE'])
def excluir_filme(id):
    dados = ler_dados()
    novos_dados = [f for f in dados if f['id'] != id]
    
    if len(novos_dados) < len(dados):
        salvar_dados(novos_dados)
        return jsonify({"mensagem": "Filme removido com sucesso"}), 200
    return jsonify({"erro": "Filme não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)