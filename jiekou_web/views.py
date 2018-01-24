#coding=utf-8
import model
from flask import Flask,render_template

app=Flask(__name__)


@app.route('/')
def index():
    return render_template("jiekou.html",title='tj')
@app.route("/login",methods=['POST', 'GET'])
def login():
    model.savedata()
    return "<h1>sss</h1>"
@app.route('/interface',methods=['POST', 'GET'])
def interface():
    model.interface_access()
    return model.interface_access()
@app.route('/see')
def see():
    return render_template("jiekou.html", title='yt')
@app.route('/demo')
def demo():
    # d = {'data':[{"city":"a", "classify":"b", "experience":"225", \
    # "id":"10000" , "logins":"24", "score":"57", "sex":"c", "sign":"d", "username":"user", "wealth":"82830700"}]}
    d='{"code":0,"msg":"","count":1000,"data":[{"id": "a", "case": "b", "name": 225 , "md": 10000, "path": 24, "data": 57, "harder": "c", "jcd": "d", "time": "user", "r": 82830700}]}'
    return d



if __name__=='__main__':
    app.run(host='172.16.3.12',debug=True)
    # app.run(host='192.168.43.102', debug=True)
