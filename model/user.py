from app import db


class Users(db.Model):
    __table_name__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(320), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password 

    def __repr__(self):
        return '<User %r %r %r>' % (self.name, self.email, self.password) 


