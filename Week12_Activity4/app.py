from flask import Flask, render_template, url_for

app = Flask(__name__)

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Image page
@app.route("/show-image")
def show_image():
    # URL of the image in static folder
    img_url = url_for('static', filename='my_image.jpg')
    return f'<h2>Here is your image:</h2><img src="{img_url}" alt="My Image">'

if __name__ == "__main__":
    app.run(debug=True)