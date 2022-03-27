import json

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template('index.html', title='Домашняя страница',
                           username=user)


@app.route("/room/<gender>/<age>")
def training(gender, age):
    if "female" in gender.lower():
        if int(age) >= 21:
            return render_template("param.html",
                                   room="Оформление каюты",
                                   path_to_image=url_for("static",
                                                         filename="img/female_21.jpg"),
                                   path_to_image_2=url_for("static",
                                                         filename="img/adult.jpg"))
        else:
            return render_template("param.html",
                                   room="Оформление каюты",
                                   path_to_image=url_for("static",
                                                         filename="img/female_no_21.jpg"),
                                   path_to_image_2=url_for("static",
                                                         filename="img/child.jpg"))
    else:
        if int(age) >= 21:
            return render_template("param.html",
                                   room="Оформление каюты",
                                   path_to_image=url_for("static",
                                                         filename="img/male_21.jpg"),
                                   path_to_image_2=url_for("static",
                                                         filename="img/adult.jpg"))
        else:
            return render_template("param.html",
                                   room="Оформление каюты",
                                   path_to_image=url_for("static",
                                                         filename="img/male_no_21.jpg"),
                                   path_to_image_2=url_for("static",
                                                         filename="img/child.jpg"))


if __name__ == '__main__':
    app.run(port=8088, host='127.0.0.1')