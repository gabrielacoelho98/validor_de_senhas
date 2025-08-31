from flask import Flask, render_template_string, request
import re

app = Flask(__name__)

# Função que valida a senha
def validar_senha(senha):
    erros = []
    if len(senha) < 8:
        erros.append("Senha deve ter pelo menos 8 caracteres")
    if not re.search(r"[A-Z]", senha):
        erros.append("Senha deve conter pelo menos uma letra maiúscula")
    if not re.search(r"[a-z]", senha):
        erros.append("Senha deve conter pelo menos uma letra minúscula")
    if not re.search(r"[0-9]", senha):
        erros.append("Senha deve conter pelo menos um número")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        erros.append("Senha deve conter pelo menos um caractere especial")
    return erros

@app.route("/", methods=["GET", "POST"])
def home():
    mensagem = ""
    erros = []
    if request.method == "POST":
        senha = request.form.get("senha")
        erros = validar_senha(senha)
        if not erros:
            mensagem = "Senha válida!"

    html = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Validador de Senhas</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f5f5f5;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                width: 350px;
                text-align: center;
            }
            h1 {
                font-size: 22px;
                margin-bottom: 20px;
                color: #333;
            }
            input[type="password"] {
                width: 100%;
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 6px;
                font-size: 14px;
            }
            button {
                background: #4CAF50;
                color: white;
                padding: 10px 15px;
                border: none;
                border-radius: 6px;
                font-size: 14px;
                cursor: pointer;
                width: 100%;
            }
            button:hover {
                background: #45a049;
            }
            p.success {
                color: green;
                font-weight: bold;
            }
            ul {
                list-style: none;
                padding: 0;
                margin-top: 10px;
                color: red;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Validador de Senhas</h1>
            <form method="POST">
                <input type="password" name="senha" placeholder="Digite sua senha">
                <button type="submit">Validar</button>
            </form>

            {% if mensagem %}
                <p class="success">{{ mensagem }}</p>
            {% endif %}

            {% if erros %}
                <ul>
                    {% for erro in erros %}
                        <li>{{ erro }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
        </div>
    </body>
    </html>
    """
    return render_template_string(html, mensagem=mensagem, erros=erros)

if __name__ == "__main__":
    app.run(debug=True)
# Rodar o aplicativo Flask  