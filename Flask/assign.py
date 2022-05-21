from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def rootfunc():
    return render_template('form.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method == 'POST':
        # name= request.form['name']
        # phy = request.form['phy']
        # chem= request.form['chem']
        # math= request.form['math']
        # dict={'Maths':math, 'Chemistry': chem, 'Physics': phy, 'Name': name}
        return render_template('resultTable.html', data= request.form)

if __name__ == '__main__':
    app.run(debug=True)