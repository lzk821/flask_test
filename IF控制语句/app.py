from flask import Flask,url_for,render_template

app = Flask(__name__)

@app.route('/index')
def index():
    age=20
    return render_template('index.html',age= age)

if __name__ == '__main__':
    app.run()
