from flask import Flask, session
from flask import render_template
from flask import request
from flask import redirect, url_for
import re

app = Flask(__name__, template_folder='template')

dic = {}


@app.route("/")
def hello_world():
    return str(dic)

@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')

@app.route('/searchPost',  methods=['POST'])
def searchPost():
    Search = request.form.get('Search')
    
    if check_content(Search) == False:
        return redirect(url_for('search'))
    else:
        session['id'] = Search
        return redirect(url_for('searchSuccess'))
        
@app.route('/searchSuccess', methods=['GET'])
def searchSuccess():
    successMessage=session['id']
    return render_template('Success.html', successMessage=successMessage)

# Check input content
def check_content(data):
    regex = r'''^[A-Za-z0-9,.!#$%&+\/=?^_`{|}~()"\- ]+$'''
    regex2 = r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))'''

    temp_data = str(data).strip()

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
        return True

if __name__== "__main__": 
    app.config['SECRET_KEY'] = '192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
