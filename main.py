from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from enhub-cloud-interns via Cloud Run and Cloud Deploy!"
