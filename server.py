import random

from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key='secret'

@app.route('/')
def greatNumberGame():
    if 'counter' in session:
        session.pop('counter')
    session['actual']=(int(random.random()*100))
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    if 'counter' not in session:
        session['counter']=1
    else:
        session['counter']+=1
    session['number']=int(request.form['number'])
    print(session)
    return redirect ('/answer')

@app.route('/answer')
def answer():
    return render_template("answer.html")

if __name__=="__main__":
    app.run(debug=True)