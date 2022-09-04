from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world!!!'

@app.route('/')
def about():
    return 'this is the about us page!'

@app.route('/')
def contact():
    return 'haha im not actually going to put my information here'
if __name__ == '_main_':
    app.run(debug=True, host='34.171.176.230', port=80)

