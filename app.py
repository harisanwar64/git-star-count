"""
info: flask API page: Controller
@author: Haris Anwar <harisanwar64@gmail.com>
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    """After accessing url (with port) the page user will see is home page.
    Home page resides in template directory with name page.html"""
    return render_template('page.html')

if __name__ == '__main__':
    app.run(debug=True)
