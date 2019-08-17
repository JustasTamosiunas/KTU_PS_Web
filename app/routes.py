from app import app
from flask import render_template, redirect, url_for, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        if request.form['answer'] == 'Amandas':
            return redirect('https://discord.gg/JaHD9ZC')
    return render_template('verify.html')