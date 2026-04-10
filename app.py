from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    tarefa = None
    erro = None

    if request.method == 'POST':
        try:
            #receber os dados
            tarefa = request.form.get('tarefa')

            #lógica do exercicio
            if tarefa:

            else:

        except ValueError:
            erro = "Informação inválida, digite números válidos."
        except Exception as erro2:
            erro = f"Ocorreu um erro inesperado: {erro2}"

    return render_template('index.html', inicial=inicial, juros=juros, meses=meses, montante=montante, erro=erro, juros_calc=juros_calc)

if __name__ == '__main__':
    app.run(debug=True, port=5000)