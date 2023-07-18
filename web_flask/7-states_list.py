#!/usr/bin/python3
"""
Write a sctript that starts flask web app 
"""
from flask import Flask, render_template
from flask import stort storage 

app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(exception)
    """tear down session"""
    storage.close


@app.route('/states_list', strict_slashes=False)
def states_list():
    """list states"""
    states = storage.all("States")
    return render_template('7-states_list.html', states=states.value()))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)