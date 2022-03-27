import json
import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/member')
def member():
    with open("members", "r", encoding="utf-8") as f:
        member_list = json.load(f)
        num = random.randint(0, (len(member_list) - 1))
        s = ", ".join(sorted(member_list[num]["specialization"]))
    return render_template('members.html', members=member_list, num=num, s=s)


if __name__ == '__main__':
    app.run(port=8100, host='127.0.0.1')