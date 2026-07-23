from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(100), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)
    access_level = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<Agent {self.nickname}>'