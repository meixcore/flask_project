from flask import Flask, render_template, request, redirect, url_for
from app.models import Agent
from app.extensions import db
from app.utils import generate_nickname

def register_routes(app):
    @app.route('/')
    def agents_list():
        access_level = request.args.get('access_level')
        if access_level:
            agents = Agent.query.filter_by(access_level=access_level).all()
        else:
            agents = Agent.query.all()
        return render_template('agents.html', agents=agents)

    @app.route('/agent/<int:id>')
    def agent_detail(id):
        agent = Agent.query.get_or_404(id)
        return render_template('agent_detail.html', agent=agent)

    @app.route('/add', methods=['GET', 'POST'])
    def add_agent():
        if request.method == 'POST':
            nickname = request.form.get('nickname', '').strip()
            number = request.form['number']
            email = request.form['email']
            access_level = request.form['access_level']

            if not nickname:
                nickname = generate_nickname()

            if nickname.strip() and number.strip() and email.strip():
                new_agent = Agent(
                    nickname=nickname,
                    number=number,
                    email=email,
                    access_level=access_level
                )
                db.session.add(new_agent)
                db.session.commit()
            return redirect(url_for('agents_list'))
        return render_template('add_agent.html', random_nickname=random_nickname)

    @app.route('/edit/<int:id>', methods=['GET', 'POST'])
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
            return redirect(url_for('agents_list'))
        return render_template('edit_agent.html', agent=agent)

    @app.route('/delete/<int:id>')
    def delete_agent(id):
        agent = Agent.query.get_or_404(id)
        db.session.delete(agent)
        db.session.commit()
        return redirect(url_for('agents_list'))