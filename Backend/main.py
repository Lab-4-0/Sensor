from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/teste', methods=['GET', 'POST'])
def teste(a='asd'):
    print (f'So um teste - {a}')
    return index()
app.run()