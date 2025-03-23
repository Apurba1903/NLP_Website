from flask import Flask, render_template, request, redirect, session
from db import Database
from api import API


app = Flask(__name__)
dbo = Database()
api = API()
app.secret_key = 'run_por_favor'

@app.route('/')
def index():

    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    
    response = dbo.insert(name, email, password)
    
    if response:
        return render_template('login.html', message='Registered Successfully. Kindly Login.', message_type='success')
    else:
        return render_template('register.html', message='Email Already Exists. Kindly Login.')
    
    
@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    
    response = dbo.search(email, password)
    
    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html', message='Incorrect Email / Password.', message_type='error')


@app.route('/profile')
def profile():
    if session.get('logged_in', 0) == 1:
        return render_template('profile.html')
    else:
        return redirect('/')



@app.route('/ner')
def ner():
    if session.get('logged_in', 0) == 1:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner', methods=['POST'])
def perform_ner():
    if session.get('logged_in', 0) == 1:
        text = request.form.get('ner_text')
        response = api.ner(text)  # Call the ner function from API class
        
        if "error" in response:
            return "NER API failed. Try again later."
        
        
        return render_template('ner.html', response=response)
    else:
        return redirect('/')



@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')



@app.route('/abuse')
def abuse():
    return render_template('abuse.html')



app.run(debug=True)