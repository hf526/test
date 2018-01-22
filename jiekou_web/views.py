#coding=utf-8
from flask import Flask,render_template,request
import  model

app=Flask(__name__)


@app.route("/login",methods=['POST', 'GET'])
def login():
    model.savedata()
    return "<h1>sss</h1>"
@app.route('/')
def index():
    return render_template("jiekou.html")

if __name__=='__main__':
    app.run(host='192.168.43.102',debug=True)

