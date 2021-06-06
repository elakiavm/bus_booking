from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session
import sqlite3 as sql
import os

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def start ():

    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']

        return redirect(url_for('user'))
    return render_template('userlogin.html')

if __name__ =="__main__":
    app.secret_key=os.urandom(24)
    app.run(debug=True)