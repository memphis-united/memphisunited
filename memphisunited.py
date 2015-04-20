import os
from flask import Flask, render_template, flash, redirect
from forms import EmailForm

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = EmailForm()
    return render_template('form.html',
                           title='Contact Rep',
                           form=form)