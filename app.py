from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Greeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

@app.route('/')
def index():
    name = request.args.get('name')
    if name:
        greeting = Greeting(name=name)
        db.session.add(greeting)
        db.session.commit()
    greeting_list = Greeting.query.all()
    return render_template('base.html', greeting_list=greeting_list, name=name)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
