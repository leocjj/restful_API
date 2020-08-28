#coding: utf-8
"""
Start a Flask web application on port 5000
https://flask.palletsprojects.com/en/0.12.x/api/#url-route-registrations
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """returns general response message"""
    return render_template('index.html')

@app.route('/GET', methods=['GET'])
def get():
    """return to GET request message"""
    return "Get response"

@app.route('/POST', methods=['POST'])
def post():
    """return to POST request message"""
    return "Post response"

@app.route('/PUT', methods=['PUT'])
def put():
    """return to PUT request message"""
    return "Put response"

@app.route('/DELETE', methods=['DELETE'])
def delete():
    """return to DELETE request message"""
    return "Delete response"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
