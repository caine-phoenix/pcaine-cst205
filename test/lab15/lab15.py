from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/')
def hello():
  return '<p>Student1 A. : LOL</p><p>Student2 b. : ROFL</p>'

@app.route('/nick')
def t_test():
   return render_template("template.html")