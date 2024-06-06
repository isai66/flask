from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "Hola que tal, este es el mundo de Isaí Lara Mojica con matricula 20211065 :)"


if __name__ == '__main__':
    app.run(debug=True)