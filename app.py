from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Testing that this thing updates."

group = ["Alex", "Anna", "Ariadna", "Bronagh", "Conor"]
for name in group:
   print(name)
