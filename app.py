from flask import Flask
app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
    return 'hello world!!!'

@app.route('/about')
def about():
    return 'this is the about us page!'

@app.route('/contact')
def contact():
    return 'haha im not actually going to put my information here'
if __name__ == '_main_':
    app.run(debug=True, host='0.0.0.0', port=80)

