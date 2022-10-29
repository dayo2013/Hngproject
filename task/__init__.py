from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    about_me={
        "SlackUsername":"Emmanuel","backend":True,"age":29,"bio":"I am a student, software developer. I am glad to be here to learn"
    }
    return about_me