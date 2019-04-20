from flask import Flask, render_template, session, logging, url_for, redirect, request, flash
from wtforms import Form, StringField, PasswordField, validators, TextAreaField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = "SuPeR_SeCrEt-KeY69erR"


#wtform class for registration fields and validators
class RegForm(Form):
    username = StringField('Username', [validators.Length(min=3, max=20)])
    password = PasswordField('Password', [
        validators.DataRequired(), 
        validators.EqualTo('passconf', message='Passwords do not match!')])
    passconf = PasswordField('Password Confirm')
    email = StringField('Email (optional)')
    submit = SubmitField('Submit')


#test function to check for spaces in a password  
def testPassword(password):
    '''
    Returns True is password contains whitespace
    '''
    for ch in password:
            if ch == ' ':
                return True

#test function to check for missing "@" and "." in an email, needs better defined
def testEmail(email):
    '''
    Returns True is "@" or "." is not in an email address.
    '''
    if '@' not in email:
        return True
    elif '.' not in email:
        return True


#"home" route
@app.route('/')
def index():
    return render_template('home.html')

#user signup route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    #instance of the registration form
    form = RegForm(request.form)
    if request.method == 'POST' and form.validate(): #test method and validation
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        if testEmail(email):  #test email
            flash('Your email is possibly invalid, you might want to check that!', 'warning')
        if testPassword(password):  #test password
            flash('Passwords cannot contain spaces! Try again!', 'danger')
            return redirect(url_for('signup', title='Register', form=form))
        return redirect(url_for('welcome', username=username))
    return render_template('signup.html', title='Register', form= form)

#welcome page after signup
@app.route('/welcome/<string:username>', methods=['GET', 'POST'])
def welcome(username):
    return render_template('welcome.html', username=username)


#if only it does......
if __name__ == '__main__':
    app.run(debug=True)