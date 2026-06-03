from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    mensagem = ""

    if request.method == 'POST':

       nickname = request.form.get('nickname')
       jogo = request.form.get('jogo')
       email = request.form.get('email')

       if not nickname or not jogo or not email:
           mensagem = "Preencha todos os campos obrigatórios!"

       elif len(nickname) < 4:
           mensagem = "O nickname deve possuir pelo menos 4 caracteres."

       else:
           mensagem = "Inscrição realizada com sucesso!"

    return render_template('cadastro.html', mensagem=mensagem)

@app.route('/index')
def formulario():
    return render_template('index.html')

@app.route('/validacao' , methods=['POST'])
def index():

    nome = request.form.get('nome', '').strip().title()
    email = request.form.get('email' ,'').strip().lower()
    cidade = request.form.get('cidade', '').strip().title()

    return f"""
    Nome: {nome}<br>
    Email: {email}<br>
    Cidade: {cidade}<br>
    """

if __name__ == '__main__':
    app.run(debug=True)