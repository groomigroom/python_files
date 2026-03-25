!pip install flask-ngrok
from flask import Flask
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)  # Flask 앱에 ngrok 연동

@app.route("/")
def home():
    return "Hello World! From Colab!"

if __name__ == "__main__":
    app.run()
run_with_ngrok
