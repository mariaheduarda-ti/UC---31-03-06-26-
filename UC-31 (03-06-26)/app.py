from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():

    mensagem = ""

    if request.method == 'POST':

        nome = request.form.get('nome').strip().title()
        email = request.form.get('email').strip().lower()
        telefone = request.form.get('telefone').strip()
        cpf = request.form.get('cpf').strip()
        cidade = request.form.get('cidade').strip()
        estado = request.form.get('estado').strip()
        curso = request.form.get('curso').strip()
        idade = request.form.get('idade').strip()
        senha = request.form.get('senha').strip()

        telefone = telefone.replace("(", "")
        telefone = telefone.replace(")", "")
        telefone = telefone.replace("-", "")
        telefone = telefone.replace(" ", "")

        cpf = cpf.replace(".", "")
        cpf = cpf.replace("-", "")

        if not nome or not email or not telefone or not cpf or not cidade or not estado or not curso or not idade or not senha:
            mensagem = "Preencha todos os campos obrigatórios."

        elif len(nome) < 8:
            mensagem = "Nome inválido."

        elif "@" not in email or ".com" not in email:
            mensagem = "E-mail inválido."

        elif len(telefone) != 11:
            mensagem = "Telefone inválido."

        elif len(cpf) != 11:
            mensagem = "CPF inválido."

        elif len(cidade) < 3:
            mensagem = "Cidade inválida."

        elif len(estado) != 2:
            mensagem = "Estado inválido."

        elif int(idade) < 16:
            mensagem = "Idade inválida."

        elif len(senha) < 8:
            mensagem = "Senha muito fraca."

        else:
            mensagem = f"""
Cadastro realizado com sucesso!

Nome: {nome}
E-mail: {email}
Telefone: {telefone}
CPF: {cpf}
Cidade: {cidade}
Estado: {estado}
Curso: {curso}
Idade: {idade}
"""

    return render_template('cadastro.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)