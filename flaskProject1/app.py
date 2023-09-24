from flask import Flask,request
# import config
app = Flask(__name__)

@app.route("/blog/list")
def profile():
    user_id=request.args.get("user_id")
    page_id=request.args.get("page_id")
    return "博客id为：%s，用户id为：%s"%(user_id,page_id)


if __name__ == '__main__':
    app.run()
