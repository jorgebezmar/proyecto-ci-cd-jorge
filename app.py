from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola, soy Jorge y esta es la prueba para el video"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
