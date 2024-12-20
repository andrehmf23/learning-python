
#_____________________________________________Desenvolvimento Web com Flask____________________________________________

# Importar pacotes
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
  return "<h1>WELCOME to My Home Page</h1>"

@app.route("/<name>")
def user(name):
  return f"<h3>Hello, nice to meet you {name}!</h3>"

@app.route("/admin")
def admin():
  return redirect(url_for("home"))

if __name__ == "__main__":
  app.run()