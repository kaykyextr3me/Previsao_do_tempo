from flask import Flask, render_template, request, make_response
import func

app = Flask(__name__)


@app.route('/')
def homepag():
    cidade = 'brasília'
    previsao = func.previsao_atual(cidade)
    return render_template('index.html', previsao=previsao)


@app.route('/', methods=['POST', 'GET'])
def busca_cidade():
    cidade = request.form['nome_cidade']
    previsao = func.previsao_atual(cidade)

    return render_template('index.html', previsao=previsao)


app.run(debug=True)
