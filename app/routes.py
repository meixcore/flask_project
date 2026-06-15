from flask import render_template, request, redirect, url_for

from app import app

@app.route('/')
def home():
    return render_template("index.html")

# @app.route('/submit', methods=['POST', 'GET'])
# def submit():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         email = request.form.get('email')
#         color = request.form.get("color")
#         profession = request.form.get("profession")
#         hobbies = request.form.getlist("hobbies")
#         level = request.form.get("level")
#         return render_template("result.html", name=name, email=email, color=color, profession=profession, hobbies=hobbies, level=level)
#     else:
#         return redirect(url_for('form'))
@app.route('/about')
def about():
    return render_template("about.html")

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

        success_message = 'Your message was sent successfully!'

    return render_template(
        'contact.html',
        success_message=success_message
    )