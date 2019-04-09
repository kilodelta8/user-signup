from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)