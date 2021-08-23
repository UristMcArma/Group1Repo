from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Testing that this thing updates and that I smell."

group = ["Alex", "Anna", "Ariadna", "Bronagh", "Conor"]
for name in group:
   print(name)