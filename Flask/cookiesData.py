from flask import Flask, render_template, request, make_response
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/setcookie', methods=['POST'])
def setCookie():
    if request.method == 'POST':
        user = request.form['userid']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userid', user)
        return resp


@app.route('/getcookie')
def getCookie():
    userid = request.cookies.get('userid')
    return '<h1>Cookie found: ' + userid + '</h1>'


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port='8080')
