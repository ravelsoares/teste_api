from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World'

@app.route('/<name>')
def name(name):
    return f'Olá, {name}'

if __name__ == '__main__':
    app.run()