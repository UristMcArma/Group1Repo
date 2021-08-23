from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Testing that this thing updates."
