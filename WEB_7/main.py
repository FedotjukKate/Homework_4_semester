import json

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/results/<name>/<level>/<rating>")
def results(name, level, rating):
    return render_template("results.html", name=name, level=level, rating=rating)


if __name__ == '__main__':
    app.run(port=8104, host='127.0.0.1')