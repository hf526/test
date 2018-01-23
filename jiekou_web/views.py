#coding=utf-8
import model
from flask import Flask,render_template

app=Flask(__name__)


@app.route('/')
def index():
    return render_template("jiekou.html")
@app.route("/login",methods=['POST', 'GET'])
def login():
    model.savedata()
    return "<h1>sss</h1>"
@app.route('/interface',methods=['POST', 'GET'])
def interface():
    model.interface_access()
    return model.interface_access()


if __name__=='__main__':
    app.run(host='172.16.3.12',debug=True)

