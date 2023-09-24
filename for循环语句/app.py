from flask import Flask,render_template

app = Flask(__name__)


@app.route('/control')
def control_statement():  # put application's code here
    age = 19
    bars = [{
        "name":"起点",
        "money":5
    },{
        "name": "沸点",
        "money": 5
    },
        {
            "name": "乐园",
            "money": 5
    }]
    return render_template("control.html", bars=bars,age=age)


if __name__ == '__main__':
    app.run()
