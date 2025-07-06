from flask import Flask, request, jsonify
import pymysql.cursors
from flask_cors import CORS

app = Flask(__name__)
CORS(app) #permite acesso ao front end

def conectar():
    return pymysql.connect(
        host='Coloque sua host',
        user='Coloque seu user',
        password='Coloque seu password',
        database='Coloque seu database',
        cursorclass=pymysql.cursors.DictCursor
    )

# Criar Rota
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    conexao = conectar()
    cursor = conexao.cursor()
    comando_get = 'SELECT * FROM vendas'
    cursor.execute(comando_get)
    produtos = cursor.fetchall()
    conexao.close()
    return jsonify(produtos)

@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    data = request.get_json()
    nome = data['nome_produto']
    valor = data['valor']

    conexao = conectar()
    cursor = conexao.cursor()
    comando_add = 'INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)'
    cursor.execute(comando_add, (nome, valor))
    conexao.commit()
    conexao.close()
    return jsonify({'mensagem': f'Produto {nome} adicionado com sucesso!'})

@app.route('/produtos/<int:id>', methods=['PUT'])
def editar_produto(id):
    data = request.get_json()
    novo_valor = data['valor']

    conexao = conectar()
    cursor = conexao.cursor()
    comando_edit = 'UPDATE vendas SET valor = %s WHERE id = %s'
    cursor.execute(comando_edit, (novo_valor, id))
    conexao.commit()
    conexao.close()
    return jsonify({'mensagem': f'Produto editado com sucesso!'})

@app.route('/produtos/<int:id>', methods=['DELETE'])
def deletar_produto(id):

    conexao = conectar()
    cursor = conexao.cursor()
    comando_deletar = 'DELETE FROM vendas WHERE id = %s'
    cursor.execute(comando_deletar, (id, ))
    conexao.commit()
    conexao.close()
    return jsonify({'mensagem': f'Produto deletado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True)
