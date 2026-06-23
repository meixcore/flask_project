import datetime

from flask import render_template, request, redirect, url_for

from app import app

@app.route('/')
def home():
    current_time = datetime.datetime.now()
    return render_template("index.html", current_time=current_time)

@app.route('/about')
def about():
    team_members = [
        {'name': 'Alice', 'role': 'Developer'},
        {'name': 'Bob', 'role': 'Designer'},
        {'name': 'Charlie', 'role': 'Project Manager'},
    ]

    return render_template("about.html", team_members=team_members, user_info=user_info)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    success_message = None

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        print(name)
        print(email)
        print(message)

        success_message = (f'{name}, your message: "{message}" was sent successfully !'
                           f'You will receive an email at {email}')

    user_info = {
        'name': 'Charlie',
        'address': {
            'street': '123 Main',
            'city': 'Wonderland',
            'zip': '12345'
        }
    }

    return render_template('contact.html',success_message=success_message, user_info=user_info)