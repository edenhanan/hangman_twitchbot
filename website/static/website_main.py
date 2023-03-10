from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def game():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("home.html", content="Hello")

if __name__ == "__main__":
    app.run(debug=True)