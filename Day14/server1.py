from flask import Flask

app = Flask(__name__)

# declare the endpoint url for the function
@app.route('/', methods=['GET'])
def hello_world():
    return "This is a message says Hello world"


if __name__ == '__main__':
    app.run()
