import json
from flask import Flask, render_template, abort

app = Flask(__name__)

def carregar_jogos():
    try:
        with open('jogos.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@app.route('/')
def home():
    lista_jogos = carregar_jogos()
    total_jogos = len(lista_jogos)
    return render_template('index.html', projetos=lista_jogos, total=total_jogos)

if __name__ == '__main__':
    app.run(debug=True)
