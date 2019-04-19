from flask import Flask, render_template, session, logging, url_for, redirect, request, flash
from wtforms import Form, StringField, PasswordField, validators, TextAreaField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = "SuPeR_SeCrEt-KeY69erR"


class RegForm(Form):
    username = StringField('Username', [validators.Length(min=3, max=20)])
    password = PasswordField('Password', [
        validators.DataRequired(), 
        validators.EqualTo('passconf', message='Passwords do not match!')])
    passconf = PasswordField('Password Confirm')
    submit = SubmitField('Submit')

    

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegForm(request.form)
    if request.method == 'POST' and form.validate():
        username = request.form['username']
        return redirect(url_for('welcome', username=username))
    return render_template('signup.html', title='Register', form= form)


@app.route('/welcome/<string:username>', methods=['GET', 'POST'])
def welcome(username):
    return render_template('welcome.html', username=username)


if __name__ == '__main__':
    app.run(debug=True)