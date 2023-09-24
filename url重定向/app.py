from flask import Flask,request,redirect

app = Flask(__name__)


@app.route('/login')
def login():  # put application's code here
    return 'login page'

@app.route('/profile')
def profile():  # put application's code here
    name = request.args.get('name')

    if not name:
        return redirect('/login')
    else:
        return name
if __name__ == '__main__':
    app.run()
