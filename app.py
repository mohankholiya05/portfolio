from flask import Flask,render_template,request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


@app.route("/")
def first():
    return render_template("index.html")
@app.route("/contact", methods = ['GET', 'POST'])
def Contact_mohit():
    
    return render_template('contact.html')
if(__name__=='__main__'):
    app.run(debug=True)