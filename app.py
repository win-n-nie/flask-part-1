from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/other')
def about():
    return 'this the about us page!'

@app.route('/next')
def contact():
    return 'haha im not going to put my information here'


if __name__ == '_main':
    app.run(debug=True, host= '0.0.0.0', port=443)

