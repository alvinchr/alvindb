from flask import Flask, render_template, request
from datetime import datetime
from waitress import serve

app = Flask(__name__)

@app.route("/")
def index():
    X = "作者:洪友錦<br>"
    X += "<a href=/db>課程網頁</a><br>"
    X += "<a href=/alvin?nick=hello>個人介紹及系統時間</a><br>"
    X += "<a href=/account>表單傳值</a><br>"
    return X

@app.route("/db")
def db():
    return "<h1><a href='https://csim.pu.edu.tw/'>資訊管理</a>導論</h1>"

@app.route("/alvin", methods=["GET", "POST"])
def alvin():
    now = str(datetime.now())
    user = request.values.get("nick")
    return render_template("alvin.html",datetime=now, name=user)

@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd
        return result

    else:
        return render_template("account.html")

if __name__ == "__main__":
    #app.run()
    serve(app, host='0.0.0.0', port=8080)
