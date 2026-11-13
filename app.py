from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from my first DevOps project!"

@app.route("/about")
def about():
    return "This is a simple Flask app running inside Docker."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
