from app import app

@app.route('/')
def hello():
    return 'Hello, Flask!'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/info')
def info():
    return 'This is an informational page.'

@app.route('/reverse/<string:name>')
def reverse(name):
    if len(name) < 2:
        return f'Слишком короткое имя'
    if not name.isalpha():
        return 'Имя должно содержать только буквы'
    return name[::-1]

@app.route('/user/<name>/<int:age>')
def user(name, age):
    if age < 0 or age > 100:
        return 'Возраст должен быть больше 0, но меньше 100'
    return f'Hello, {name}! You are {age} years old.'

@app.route('/calc/<int:num1>/<int:num2>')
def calc(num1, num2):
    return f"The summ of {num1} and {num2} is {num1 + num2}"