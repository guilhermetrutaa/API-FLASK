# API de Produtos com Flask e MySQL

Esta é uma API simples para gerenciamento de produtos, construída em Python utilizando Flask e MySQL (via PyMySQL). A API permite listar, adicionar, editar e deletar produtos armazenados em uma tabela chamada `vendas`.

---

## Tecnologias utilizadas

- Python 3.x  
- Flask  
- PyMySQL  
- Flask-CORS (para permitir requisições do front-end)  
- MySQL (banco de dados relacional)  

---

## Funcionalidades

- **Listar produtos** (`GET /produtos`): Retorna a lista de todos os produtos cadastrados.  
- **Adicionar produto** (`POST /produtos`): Adiciona um novo produto com nome e valor.  
- **Editar produto** (`PUT /produtos/<id>`): Atualiza o valor de um produto pelo seu ID.  
- **Deletar produto** (`DELETE /produtos/<id>`): Remove um produto pelo seu ID.  

---

## Estrutura da tabela `vendas`

A tabela no banco de dados MySQL deve conter, pelo menos, os seguintes campos:

| Campo        | Tipo          | Observação                  |
|--------------|---------------|-----------------------------|
| id           | INT           | Chave primária, auto-incremento |
| nome_produto | VARCHAR(...)  | Nome do produto             |
| valor        | FLOAT ou DECIMAL | Valor do produto            |

---

## Configuração

1. Clone este repositório:

   ```bash
   git clone https://github.com/guilhermetrutaa/API-FLASK.git
   cd API-FLASK
   ```

2. Instale as dependências necessárias:

   ```bash
   pip install flask pymysql flask-cors
   ```

3. Configure a conexão com o banco de dados MySQL no arquivo principal (`app.py` ou onde está o código), no método `conectar()`, substituindo:

   ```python
   host='Coloque sua host',
   user='Coloque seu user',
   password='Coloque seu password',
   database='Coloque seu database',
   ```

4. Execute a aplicação:

   ```bash
   python app.py
   ```

5. A API estará disponível no endereço: `http://localhost:5000`

---

## Exemplos de uso

### Listar produtos

```bash
GET http://localhost:5000/produtos
```

### Adicionar um produto

```bash
POST http://localhost:5000/produtos
Content-Type: application/json

{
  "nome_produto": "Camiseta",
  "valor": 49.90
}
```

### Editar produto

```bash
PUT http://localhost:5000/produtos/1
Content-Type: application/json

{
  "valor": 59.90
}
```

### Deletar produto

```bash
DELETE http://localhost:5000/produtos/1
```

---

## Observações

- Esta API permite requisições CORS, facilitando a integração com front-ends externos.
- Para produção, recomenda-se ajustar as configurações de debug e segurança.

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## ✉️ Contato

Guilherme Truta/guilhermetrutaa - guilhermetrutaa@gmail.com

Link Projeto:
