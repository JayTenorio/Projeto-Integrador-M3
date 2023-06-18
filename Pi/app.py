from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def mostrar_preco_combustivel():
    registros = [
        {'data': '01/01/2019', 'preco_medio': 4.5, 'preco_minimo': 4.2, 'preco_maximo': 4.8},
        {'data': '02/01/2019', 'preco_medio': 4.6, 'preco_minimo': 4.3, 'preco_maximo': 4.9},
        {'data': '03/01/2019', 'preco_medio': 4.8, 'preco_minimo': 4.4, 'preco_maximo': 5.1},
        {'data': '04/01/2019', 'preco_medio': 4.7, 'preco_minimo': 4.5, 'preco_maximo': 4.9},
        {'data': '05/01/2019', 'preco_medio': 4.9, 'preco_minimo': 4.6, 'preco_maximo': 5.2},
        {'data': '06/01/2019', 'preco_medio': 5.0, 'preco_minimo': 4.7, 'preco_maximo': 5.3},
        {'data': '07/01/2020', 'preco_medio': 5.1, 'preco_minimo': 4.8, 'preco_maximo': 5.5},
        {'data': '08/01/2020', 'preco_medio': 4.9, 'preco_minimo': 4.6, 'preco_maximo': 5.2},
        {'data': '09/01/2020', 'preco_medio': 4.7, 'preco_minimo': 4.4, 'preco_maximo': 4.9},
        {'data': '10/01/2020', 'preco_medio': 4.6, 'preco_minimo': 4.3, 'preco_maximo': 4.8},
        {'data': '11/01/2020', 'preco_medio': 4.8, 'preco_minimo': 4.5, 'preco_maximo': 5.0},
        {'data': '12/01/2020', 'preco_medio': 4.6, 'preco_minimo': 4.2, 'preco_maximo': 4.9},
        {'data': '13/01/2021', 'preco_medio': 4.7, 'preco_minimo': 4.3, 'preco_maximo': 5.1},
        {'data': '14/01/2021', 'preco_medio': 4.9, 'preco_minimo': 4.6, 'preco_maximo': 5.2},
        {'data': '15/01/2022', 'preco_medio': 5.0, 'preco_minimo': 4.7, 'preco_maximo': 5.3}
    ]

    return render_template('index.html', registros=registros)

if __name__ == '__main__':
    app.run()