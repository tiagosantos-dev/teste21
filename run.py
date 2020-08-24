from flask import Flask

app = Flask(__name__)

@app.route('/teste')
def main():
    return 'testando'

app.run(host='0.0.0.0')