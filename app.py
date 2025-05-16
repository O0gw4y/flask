from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
import os
app = Flask(__name__)
app.config.from_object('config.Config')
# Ensure instance folder exists
os.makedirs(os.path.join(app.root_path, 'instance'), exist_ok=True)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
class User(db.Model):
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(80), nullable=False)
email = db.Column(db.String(120), nullable=False)
class UserForm(FlaskForm):
name = StringField('Name', validators=[DataRequired()])
email = StringField('Email', validators=[DataRequired(), Email()])
submit = SubmitField('Submit')
@app.route('/', methods=['GET', 'POST'])
def index():
form = UserForm()
if form.validate_on_submit():
user = User(name=form.name.data, email=form.email.data)
db.session.add(user)
db.session.commit()
return redirect(url_for('index'))
users = User.query.all()
return render_template('index.html', form=form, users=users)
@app.route('/delete/<int:id>')
def delete(id):
user = User.query.get_or_404(id)
db.session.delete(user)
db.session.commit()
return redirect(url_for('index'))
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
user = User.query.get_or_404(id)
form = UserForm(obj=user)
if form.validate_on_submit():
user.name = form.name.data
user.email = form.email.data
db.session.commit()
return redirect(url_for('index'))
return render_template('update.html', form=form, user=user)
if __name__ == '__main__':
app.run(debug=True)
