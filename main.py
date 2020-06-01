from flask import Flask, redirect, url_for, request, render_template
from control.register_form import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# 注册页面
@app.route('/register', methods=["post", "get"])
def register():
    if request.method == "POST":
        requestJsonString = request.form.to_dict()
        register_form_data = register_form()
        isSecceed = register_form_data.RegisterData(requestJsonString)
        if isSecceed>0:
            return render_template('success.html')
        else:
            return render_template("failed.html")
    return render_template('register.html')


if __name__ == "__main__":
    app.run('127.0.0.1', '5000', debug=True)
