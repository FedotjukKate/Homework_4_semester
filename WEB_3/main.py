from flask import Flask, render_template, url_for
import os
from dotenv import load_dotenv
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField


class LoadImageForm(FlaskForm):
    file = FileField()
    submit = SubmitField('Войти')


load_dotenv()


app = Flask(__name__)


app.config["SECRET_KEY"] = "MySeCrEtKeY123"


@app.route("/gallery", methods=['GET'])
def web3():
    form = LoadImageForm()
    return render_template("web3.html", images=list(map(lambda x: url_for('static', filename=x),
                                                        map(lambda t: "img/" + t,
                                                            os.listdir("./static/img/")))), form=form)


if __name__ == '__main__':
    app.run(port=8097, host='127.0.0.1')