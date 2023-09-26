import wtforms
from wtforms.validators import Email, Length,EqualTo
from models import UserModel,EmailCaptchaModel
from exts import db
#Form: 主要用来验证前端提交的数据是否符合要求
class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
    captcha = wtforms.StringField(validators=[Length(min=6, max=6, message="验证码格式错误！")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="用户名长度错误！")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码长度错误！")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password",message="两次密码不一致")])

    # 自定义验证：
    # 1.邮箱是否已经被注册

    def validate_email(self,filed):
        email = filed.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.validationError(message="该邮箱已被注册！")
    # 2.验证码受否正确
    def validate_captcha(self,filed):
        captcha = filed.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email,captcha=captcha).first()
        # user = UserModel.query.filter_by(email=email).first()
        if not captcha_model:
            raise wtforms.validationError(message="邮箱或者验证码错误！")
        # todo: 可以删掉captcha_model（可以写一个脚本，定期清理）
        # else:
        #     # 数据用掉就会被删掉
        #     db.session.delete(captcha_model)
        #     db.session.commit()
        #
class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码长度错误！")])