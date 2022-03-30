from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['firstname'])
        print(request.form['lastname'])
        print(request.form['education'])
        print(request.form.getlist('add[]'))
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Заявка принята"


if __name__ == "__main__":
    app.run(port=8102, host='127.0.0.1')