# from urllib import request
from flask import Flask,request
 
app = Flask(__name__)


# @app.route("/members")
# def members():
#     return {"members":["mem1","mem2","mem3"]}


@app.route('/acceptData', methods=['GET','POST'])
def getData():
    nm = request.form.get('name')
    em = request.form.get('email')
    return data(nm,em)


@app.route('/data')
def data(nm,em):
    name = nm
    email = em
    return {"name": name, "email":email}

if __name__ == "__main__":
    app.run(debug=True)