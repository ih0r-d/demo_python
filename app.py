from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/main")
def get_hello():
    return "Hello, all !!!"


@app.route("/get/<int:n>")
def get_number(n):
    return f'Number !!! {n}'


if __name__ == '__main__':
    app.run(debug=True)
