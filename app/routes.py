from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'name': 'Azis Hapidin'}
    posts = [
        {
            'title': 'Judul A',
            'content': 'Kontent A'
        },
        {
            'title': 'Judul B',
            'content': 'Kontent B'
        }
    ]

    return render_template('home.html', user=user, posts=posts)