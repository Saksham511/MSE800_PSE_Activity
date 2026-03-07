from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask Framework!"

@app.route("/depart")
def depart():
    return "<p>See you soon!</p>"

if __name__ == "__main__":
    app.run(debug=True)