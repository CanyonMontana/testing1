from flask import Flask

app = Flask(__name__)

@app.route("/")

def hello():
    return "helloHAHA"

if __name__ == "__main__":
    print("SUCCESSFUL LAUNCH")
    app.run(host='0.0.0.0', debug=True)


