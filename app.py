from flask import Flask

app = Flask(__name__)


@app.route('/')
def HelloWorld():
  return "<h1>Ivan C. Reyes</h1>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
