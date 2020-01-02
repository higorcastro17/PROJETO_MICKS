from flask import Flask,render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/static/index.html')
def dashboard():
    return render_template('index.html')

@app.route('/static/equipamentos.html')
def equipamentos():
    return render_template('equipamentos.html')









if __name__ == '__main__':
    app.run(debug=True)
