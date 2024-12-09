from flask import Flask, render_template

### WSGI APPLICATION
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this flask course. This should be an amazing 111"

@app.route("/index")
def index():
    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)