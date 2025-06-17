from flask import Flask

app = Flask(__name__)  # Это критически важная строка

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()