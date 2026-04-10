from flask import Flask, render_template, request, redirect, url_for
import json #importa a biblioteca para manipulação de arquivos JSON
import os #importa a biblioteca para manipulação de arquivos e diretórios

app = Flask(__name__)

#Configurações para o arquivo JSON
PASTA_DO_PROJETO = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_DB = os.path.join(PASTA_DO_PROJETO, 'db.json')

#Função para ler os dados do arquivo JSON
def ler_dados():
    # Verifica se o arquivo existe, se não existir, cria um novo arquivo com um dicionário vazio
    if not os.path.exists(ARQUIVO_DB):
        setar_dados({})  # Cria o arquivo com um dicionário vazio se não existir
        return {}
    
    with open(ARQUIVO_DB, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}  # Retorna um dicionário vazio se o arquivo estiver vazio ou corrompido

#Função para escrever os dados no arquivo JSON
def setar_dados(dados):
    with open(ARQUIVO_DB, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# --- ROTAS DO CRUD ---

# 1. READ - Listar tarefas
@app.route('/')
def index():
    tarefas = ler_dados()
    return render_template('index.html', tarefas=tarefas)

# 2. CREATE - Adicionar nova tarefa
@app.route('/criar', methods=['POST'])
def criar():
    nova_tarefa = request.form.get('tarefa')
    if nova_tarefa:
        tarefas = ler_dados()
        novo_id = str(len(tarefas) + 1)  # Gera um novo ID incremental
        tarefas[novo_id] = {
            'descricao': nova_tarefa,
            'status': 'pendente'
        }
        setar_dados(tarefas)
    return redirect(url_for('index'))

# 3. UPDATE - Alterar status da tarefa
@app.route('/atualizar/<int:id_tarefa>', methods=['POST'])
def atualizar(id_tarefa):
    tarefas = ler_dados()
    if 0 <= id_tarefa < len(tarefas):
        tarefas[id_tarefa] = request.form['tarefa']
        setar_dados(tarefas)
    return redirect(url_for('index'))

# 4. DELETE - Remover tarefa
@app.route('/remover/<int:id_tarefa>', methods=['POST'])
def remover(id_tarefa):
    tarefas = ler_dados()
    if 0 <= id_tarefa < len(tarefas):
        tarefas.pop(id_tarefa)
        setar_dados(tarefas)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)