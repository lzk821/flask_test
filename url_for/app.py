from flask import Flask,url_for

app = Flask(__name__)


@app.route('/blog/<int:blog_id>')
def index(blog_id):  # put application's code here
    return '您查找的博客id为：%s' %blog_id
@app.route('/urlfor')
def get_url_for():  # put application's code here
    url=url_for('index',blog_id=2,user='liash')
    return url


if __name__ == '__main__':
    app.run()
