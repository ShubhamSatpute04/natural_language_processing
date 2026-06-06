from doctest import debug

from flask import Flask, redirect,url_for
app=Flask(__name__)

@app.route('/')
def hello_world():
    return ('Hello world')

@app.route('/hello')
def hello_index():
    return('Welcome to Python Programming')

# variable arguments like * in node
@app.route('/hello/<name>')
def greet(name):
    return f'hello {name}'

# redirection 

@app.route('/admin')
def hello_admin():
    return 'This is a admin page'

@app.route('/admin/<guest>')
def admin_greet(guest):
    return f'Welcome guestn {guest}'

@app.route('/user/<name>')
def hello_user(name):
    if name== 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_user',guest=name))



if __name__=='__main__':
    app.run(debug=True)