from flask import Flask
from SecondPage import FlaskBP

app = Flask(__name__)
app.register_blueprint(FlaskBP)

@app.route("/")
def hello():
    return "Hello, World!"


if __name__ == "__main__":
    app.run()