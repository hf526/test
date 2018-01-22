#coding=utf-8
from flask import Flask,render_template


app=Flask(__name__)

@app.route("/login",methods=['POST', 'GET'])
def login():
    return "<h1>hello</h1>"

@app.route('/')
def index():
    return render_template("jiekou.html")

if __name__=='__main__':
    app.run()

