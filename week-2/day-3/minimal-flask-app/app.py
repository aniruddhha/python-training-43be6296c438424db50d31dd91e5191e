from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")  # decorator
def hello_world():

    al = "<script>alert('hi')</script>"
    return(
        f'''
            Hello, World! Welcome to Flask
            {escape(al)}
        '''
    )


@app.route("/abc")
def hello_abc():
    return "<p>Returninng ABC</p>"


@app.route("/pqr")
def hello_pqr():
    return "<p>Returninng PWR</p>"
