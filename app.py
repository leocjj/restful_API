#coding: utf-8
"""
Start a Flask web application on port 5000
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    """returns general response message"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port='5000')
