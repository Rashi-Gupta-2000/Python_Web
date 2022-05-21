from flask import Flask, redirect, url_for, request, abort
app = Flask(__name__)


@app.route("/hello/<name>")  # two parameters (rule, options)
def hello_world(name):
    return "Hello %s" % name


@app.route("/post/<int:postid>")
def hello_post(postid):
    return "Hello %d" % postid


@app.route('/admin')
def hello_admin():
    return "hello admin"


@app.route("/guest/<guest>")
def hello_guest(guest):
    return "hello %s as guest" % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))
# app.add_url_rule('/', view_func=hello_world)

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        if request.form['nm'] == 'admin':
            return redirect(url_for('success', name=user))
        else:
            abort(400)
    else:
        user= request.args.get('nm')
        return redirect(url_for('success', name=user))

@app.route('/userData')
def userData():
    user = request.args.get('nm')
    return redirect(url_for('success', name=user))

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' %name 

if __name__ == '__main__':
    app.run( debug=True, host ='127.0.0.1', port=8000)
