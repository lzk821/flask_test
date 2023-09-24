from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_migrate import Migrate

app = Flask(__name__)

HOSTNAME = '127.0.0.1'
PORT = 1116
USERNAME = 'root'
password = 'password'
DATEBASE = 'learn'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{USERNAME}:{password}@{HOSTNAME}:{PORT}/{DATEBASE}?charset=utf8mb4'
db =SQLAlchemy(app)

class User(db.Model):
    __tableanme__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100))
    articles=db.relationship("Article",back_populates="author")


class Article(db.Model):
    __tableanme__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    author_id=db.Column(db.Integer,db.ForeignKey("user.id"))
    author = db.relationship("User", back_populates="articles")

# with app.app_context():
#     db.create_all()
migrate = Migrate(app,db)

@app.route('/user')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/user/add')#增(用户)
def user_add():
    #1.创建ORM对象
    user=User(username="liash",password="111621")
    #2.将ORM对象添加到db.session中
    db.session.add(user)
    #3. 将db.sesssion中的改变同步到数据库中
    db.session.commit()
    return "用户创建成功"

@app.route('/article/add')#增（文章）
def article_add():
    article1=Article(title="python基础",content="请访问www.liash.link")
    article1.author = User.query.get(1)

    article2 = Article(title="flask基础", content="请访问www.liash.link")
    article2.author = User.query.get(1)
    #2.将ORM对象添加到db.session中
    db.session.add_all([article1,article2])
    #3. 将db.sesssion中的改变同步到数据库中
    db.session.commit()
    return "用户创建成功"

@app.route('/user/delate')#删
def user_delete():
    #1.创建ORM对象
    user = User.query.filter_by(username="liash").first()
    #2.从db.session中删除
    db.session.delete(user)
    #3. 将db.sesssion中的改变同步到数据库中
    db.session.commit()
    return "数据删除成功"

@app.route('/user/updata')#改
def user_updata():
    #1.这里返回的是一个user对象而不是query对象
    # user=User.query.filter_by(username="liash")[0]切片操作，但如果数据为空会报错
    user = User.query.filter_by(username="liash").first()
    #2.将ORM对象添加到db.session中
    user.password = "20000821"
    #3. 将db.sesssion中的改变同步到数据库中
    db.session.commit()
    return "数据修改成功"

@app.route('/user/query')#查(user)
def user_query():
    #1. get查找
    # user=User.query.get(1)
    # print(f"{user.id}:{user.username}--{user.password}")

    #2.filter_by查找
    #query:类数组
    users=User.query.filter_by(username="liash")
    for user in users:
        print(user.username)
    return "数据查找成功"

@app.route('/article/query')#查(article)
def article_query():
    #1. get查找
    user=User.query.get(1)
    for article in user.articles:
        print(article.title)
    return "数据查找成功"


if __name__ == '__main__':
    app.run()
