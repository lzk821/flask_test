from flask import Flask

app = Flask(__name__)


@app.route('/blog/add',methods=['post'])
def hello_world():  # put application's code here
    return '这是一个post方法'


if __name__ == '__main__':
    app.run()
