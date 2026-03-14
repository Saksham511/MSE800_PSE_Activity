from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello Flask!</p>"

@app.route("/depart")
def depart():
    return "<p>See you soon!</p>"

@app.route("/username/<name>")
def portal(name):
    return f"{name} is online"

@app.route("/username/<name>/<int:number>")
def marks(name,number):
    return f"{name} is online. He scored {number} in exam."

if __name__ == "__main__":
    app.run(debug=True)