from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Agent, db
from app.utils import generate_nickname

main_blueprint = Blueprint("main", __name__)


@main_blueprint.route('/')
def agents_list():
    access_level = request.args.get('access_level')
    if access_level:
        agents = Agent.query.filter_by(access_level=access_level).all()
    else:
        agents = Agent.query.all()
    return render_template('agents.html', agents=agents)

@main_blueprint.route('/agent/<int:id>')
def agent_detail(id):
    agent = Agent.query.get_or_404(id)
    return render_template('agent_detail.html', agent=agent)

@main_blueprint.route('/add', methods=['GET', 'POST'])
def add_agent():
    if request.method == 'POST':
        nickname = request.form.get('nickname', '').strip()
        number = request.form.get('number', '').strip()
        email = request.form.get('email', '').strip()
        access_level = request.form.get('access_level', '').strip()

        if not nickname:
            nickname = generate_nickname()

        if not number or not email or not access_level:
            return render_template(
                'add_agent.html',
                random_nickname=nickname,
                error='Заполните все обязательные поля.',
                number=number,
                email=email,
                access_level=access_level
            )

        new_agent = Agent(
            nickname=nickname,
            number=number,
            email=email,
            access_level=access_level
        )

        db.session.add(new_agent)
        db.session.commit()
        return redirect(url_for('main.agents_list'))
    return render_template('add_agent.html', random_nickname=generate_nickname())

@main_blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_agent(id):
    agent = Agent.query.get_or_404(id)
    if request.method == 'POST':
        new_nickname = request.form['nickname']
        new_number = request.form['number']
        new_email = request.form['email']
        new_access_level = request.form['access_level']
        if new_nickname.strip() and new_number.strip() and new_email.strip():
            agent.nickname = new_nickname
            agent.number = new_number
            agent.email = new_email
            agent.access_level = new_access_level
            db.session.commit()
        return redirect(url_for('main.agents_list'))
    return render_template('edit_agent.html', agent=agent)

@main_blueprint.route('/delete/<int:id>')
def delete_agent(id):
    agent = Agent.query.get_or_404(id)
    db.session.delete(agent)
    db.session.commit()
    return redirect(url_for('main.agents_list'))