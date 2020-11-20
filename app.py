#Importing functions from flask
from flask import Flask, render_template , url_for

#import sqlAalchemy from flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy


#import datetime
from datetime import datetime

#Instantaiting application referencing the file 
app = Flask(__name__)
#Inidicating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/pfsql'
#Initilise db
db = SQLAlchemy(app)


#model class
class Todo(db.Model):
    #Attributes
    id = db.Column(db.Integer, primary_key = True)
    content= db.Column(db.String(200))
    date_created= db.Column(db.DateTime , default =datetime.now())

    #Function that returns id using jinja syntax
    def __message__(self):
        return '<Task %r>' % self.id

#Creating index route
@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    #Debug set to true to indicate any errors
    #app.run starts the web server
    app.run(debug=True)