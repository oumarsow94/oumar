from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def test():
    return 'je deteste heroku'


if __name__ == "__main__":
    app.run(debug=True)