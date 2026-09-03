from flask import Flask, render_template

app = Flask(__name__)

# 1. This route loads when you first open the site (the login form)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
