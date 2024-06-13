import requests
from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello from Koyeb'

@app.route('/test1')
def test1():
    r = requests.get('https://api.github.com/users/kallolray')
    return r.content
 
@app.route('/test2')
def test2():
    r = requests.get('https://music.youtube.com/watch?v=SW2uyfNqHg4')
    return r.content

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)