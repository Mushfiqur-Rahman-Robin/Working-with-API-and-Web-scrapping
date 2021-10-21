

from flask import Flask, escape, request, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/passed/<int:score>')
def passed(score):
  res = ""
  if score < 50:
    res = 'fail'
  else:
    res = 'pass'
  exp = {'score' : score, 'res' : res}
  return render_template('result.html', result = exp)



@app.route('/failed/<int:score>')
def failed(score):
  return "The person has failed by obtaining  "  + str(score)


@app.route('/results/<int:marks>')
def results(marks):
  result = ""
  if marks < 50:
    results = "failed"
  else:
    results = "passed"
  return redirect(url_for(results, score = marks))
  


@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_score=(science+maths+c+data_science)/4
    res=""

    return redirect(url_for('passed', score = total_score))

if __name__ == "__main__":
  app.run()