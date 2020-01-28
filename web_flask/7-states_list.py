#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown:
    """  close the strorage  """
    storage.close
    
@app.route('/states_list', strict_slashes=False)
def states_list(n):
    """Display a html page"""
    states = storage.all(State)
    dict_to_html = {value.id: vadlue.name for value in states.values()}
    return render_template('7-states_list.html',
                           Table="states", items=dict_to_html) 
    



if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)