'''
from flask import Flask, request

app = Flask(__name__)


@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):  # put application's code here
    blog_id=blog_id
    return f'您访问的页面是：{blog_id}'

@app.route('/book/list')
def book_list():  # put application's code here
    page= request.args.get("page",default=1,type=int)
    return f'您访问的是第{page}页图书'


if __name__ == '__main__':
    app.run()
'''

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def first():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()