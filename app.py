from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "我的智慧監控站儀表板"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)