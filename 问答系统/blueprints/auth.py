import string,_string,random
from flask import Blueprint,render_template,request,jsonify,redirect,url_for,session
from exts import mail,cache,db
from flask_mail import Message
from models import EmailCaptchaModel,UserModel
from .forms import RegisterForm,LoginForm
from werkzeug.security import generate_password_hash,check_password_hash#自动生成加密密码

#/auth
bp = Blueprint("auth",__name__,url_prefix="/auth")

@bp.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱不存在")
                return render_template(url_for("auth/login"))
            if check_password_hash(user.password,password):
                # cookie:
                # cookie中不适合存储太多的数据，只适合存储少量的数据，一般用来存储登录授权的东西
                # falsk中的session,是经过加密后存储在cookie中的
                session['user.id'] = user.id
                return redirect("/")

            else:
                print("密码错误！")
                return redirect(url_for("auth/login"))
        else:
            print(form.errors)
            return redirect(url_for("auth/login"))


#GET： 从服务器上获取数据
#POST: 将客户端的数据提交给服务器
@bp.route("/register",methods=['GET','POST'])
def register():
    # 验证用户提交的邮箱和验证码是否对应且正确
    # 表单验证： flask-wtf: wtforms
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user=UserModel(email=email, username = username, password = generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            print(form.errors)
            return redirect(url_for("auth.register"))

@bp.route("/captcha/email")
def get_email_captcha():
    email = request.args.get("email")
    source = string.digits * 6  # 随机数组，字母，数字和字母组合
    captcha = random.sample(source,6) #采样
    captcha = "".join(captcha)
    message = Message(subject="liash注册验证码", recipients=[email], body=f"您的验证码是：{captcha}")
    mail.send(message)
    email_captcha = EmailCaptchaModel(email=email,captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    # RESTful API
    #{code: 200/400/500, message:"", data: {}}
    return jsonify({"code": 200, "message":"", "data": None})

@bp.route("/mail/test")
def mail_test():
    message = Message(subject="邮箱测试", recipients=["lzkx821@gmail.com"], body="这是一条测试邮件")
    mail.send(message)
    return "邮件发送成功"

@bp.route('/logout')
def logout():
    # 清除用户会话信息
    session.pop('user_id', None)
    return redirect(url_for('index'))  # 重定向到你的首页视图
