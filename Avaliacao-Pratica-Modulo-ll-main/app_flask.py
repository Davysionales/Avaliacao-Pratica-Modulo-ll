from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

## Continue o código aqui.

@app.route('/soma/')
def soma():
    num1 = int(request.args.get("valor1"))
    num2 = int(request.args.get("valor2"))
    return f'{num1} + {num2} = {num1 + num2}'

@app.route('/subtrair/')
def subtracao():
    num1 = int(request.args.get("valor1"))
    num2 = int(request.args.get("valor2"))
    return f'{num1} - {num2} = {num1 - num2}'

@app.route('/multiplicar/')
def multiplicacao():
    num1 = int(request.args.get("valor1"))
    num2 = int(request.args.get("valor2"))
    return f'{num1} multiplicado por {num2} é igual à: {num1 * num2}'

@app.route('/dividir/')
def divisao():
    num1 = int(request.args.get("valor1"))
    num2 = int(request.args.get("valor2"))
    if num2 == 0:
        return 'Erro! Não é possível dividir por 0'
    
    return f'{num1} divido por {num2} é igual à: {num1/num2:.2f}'





if __name__ == "__main__":
    app.run(debug=True)
