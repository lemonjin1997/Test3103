from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import re

app = Flask(__name__, template_folder='template')

dic = {}


@app.route("/")
def hello_world():
    return str(dic)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/loginPost",  methods=['POST'])
def logining():
    Username = request.form.get('Username')
    Password = request.form.get('Password')
    if dic.get(Username) is not None:
        if dic[Username] == Password:
            print('login sucess')
    return redirect(url_for('login'))

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/registerPost",  methods=['POST'])
def registering():
    Username = request.form.get('Username')
    Password = request.form.get('Password')
    dic[Username] = Password
    print(Username, Password)
    return redirect(url_for('login'))

@app.route('/search')
def search():
    return render_template('dashboard.html')

@app.route('/searchPost',  methods=['POST'])
def searchPost():
    Search = request.form.get('Search')
    if check_content():
        pass


# Check input content
def check_content(data):
    regex = r'''^[A-Za-z0-9,.!#$%&+\/=?^_`{|}~()"\- ]+$'''
    regex2 = r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))'''

    temp_data = str(self.data).strip()

    ptn = re.compile(regex)
    ptn2 = re.compile(regex2)
    
    if len(temp_data) > 500:
        print("fail 0")
        return False

    if not bool(ptn.search(temp_data)):
        print("fail 1")
        return False

    elif bool(ptn2.search(temp_data)):
        print("fail 2")
        return False

    else:
        return temp_data

if __name__== "__main__": 
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
