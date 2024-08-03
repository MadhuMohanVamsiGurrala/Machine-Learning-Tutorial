from flask import *
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    uname = request.form['uname']
    password = request.form['password']
    if uname == "vamsi" and password=="system":
        return "Welcome %s" %uname
    else:
        return "invalid %s" %uname

if __name__ == '__main__':
    app.run(debug=True)