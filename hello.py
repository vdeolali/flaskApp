from flask import Flask
app = Flask(__name__)


@app.route("/<name>")
def hello(name):
    assert isinstance(name, object)
    return "Hello from Flask App" + "      " + name

if __name__ == "__main__":
    app.run(debug=True)