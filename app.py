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

# NER Implementation

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


# Sentiment Analysis Implementation
@app.route('/sentiment')
def sentiment():
    if session.get('logged_in', 0) == 1:
        return render_template('sentiment.html')
    else:
        return redirect('/')

@app.route('/perform_sentiment', methods=['POST'])
def perform_sentiment():
    if session.get('logged_in', 0) == 1:
        text = request.form.get('sentiment_text')
        response = api.sentiment(text)  # Call the sentiment_analysis function from API class
        
        if "error" in response:
            return "Sentiment Analysis API failed. Try again later."
        
        return render_template('sentiment.html', response=response)
    else:
        return redirect('/')


# Abuse IP Check Implementation
@app.route('/abuse')
def abuse():
    if session.get('logged_in', 0) == 1:
        return render_template('abuse.html')
    else:
        return redirect('/')

@app.route('/perform_abuse_check', methods=['POST'])
def perform_abuse_check():
    if session.get('logged_in', 0) == 1:
        ip_address = request.form.get('abuse_ip')
        response = api.abuse(ip_address)  # Call the abuse_ip_check function from API class
        
        if "error" in response:
            return "Abuse IP Check API failed. Try again later."
        
        return render_template('abuse.html', response=response)
    else:
        return redirect('/')



if __name__ == "__main__":
    app.run(debug=False)