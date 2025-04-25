from flask import Flask, request, jsonify
import mysql.connector
from config import Config 
from flask import render_template

# Inicializa a aplicação Flask
app = Flask(__name__)

# Carrega configurações do arquivo config.py
app.config.from_object(Config)

# Função para estabelecer conexão com o banco de dados MySQL
def get_connection():
    return mysql.connector.connect(
        host=app.config['MYSQL_DATABASE_HOST'],
        user=app.config['MYSQL_DATABASE_USER'],
        password=app.config['MYSQL_DATABASE_PASSWORD'],
        database=app.config['MYSQL_DATABASE_DB']
    )

# Rota para cadastrar um novo aluno (método POST)
@app.route('/alunos', methods=['POST'])
def cadastrar_aluno():

    dados = request.get_json() # Obtém os dados do aluno do corpo da requisição

    nome = dados.get('nome')
    email = dados.get('email')
    matricula = dados.get('matricula')
    senha = dados.get('senha')

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO aluno (nome, email, matricula, senha) VALUES (%s, %s, %s, %s)",
                   (nome, email, matricula, senha))
    
    conn.commit() # Confirma a transação no banco

    # Encerra o cursor e a conexão com o banco
    cursor.close()
    conn.close()

    # Retorna uma mensagem de sucesso
    return jsonify({'mensagem': 'Aluno cadastrado com sucesso!'}), 201
    

# Rota para listar todos os alunos (método GET)
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    conn = get_connection()
    cursor = conn.cursor()

# Executa o comando SQL para selecionar os dados dos alunos
    cursor.execute("SELECT id, nome, email, matricula FROM aluno")
    dados = cursor.fetchall()

    alunos = []

    # Constrói a lista de alunos em formato de dicionário
    for id, nome, email, matricula in dados:
        alunos.append({
            'id': id,
            'nome': nome,
            'email': email,
            'matricula': matricula
        })

    cursor.close()
    conn.close()

    # Retorna a lista de alunos em formato JSON
    return jsonify(alunos)

# Rota para atualizar um aluno
@app.route('/')
def index():
    return render_template('index.html')

# Inicia a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)
