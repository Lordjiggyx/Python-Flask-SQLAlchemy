#Importing functions from flask
from flask import Flask, render_template , url_for , request , redirect

#import sqlAalchemy from flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy


#import datetime
from datetime import datetime

import sys
import logging


#Instantaiting application referencing the file 
app = Flask(__name__)
#Inidicating database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/pfsql'
#Initilise db
db = SQLAlchemy(app)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


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
@app.route("/", methods=['POST','GET'])
def index():

    #If method is post the todo will be added to the database
    if request.method == 'POST':
        #Get data from input which is referenced by name
        task_content = request.form['content']
        #Creating Task object with information from form
        new_task = Todo(content=task_content)

        try:
            #Adding to session
            db.session.add(new_task)
            #commiting to database
            db.session.commit()
            #Using redirect to redirect user to homepage
            return redirect('/')
        except:
            return "Error detected: Task could not be added to database"
    #Otherwise it would return the page 
    else:
        #Querys the database and returns all the items by time that they were created
        tasks = Todo.query.order_by(Todo.date_created).all()
        print(tasks)
        return render_template('index.html' , tasks = tasks)




#Method to delete object
@app.route('/delete/<int:id>')
#Takes in id para
def delete(id):
    #This will query the DB and 
    task_to_delete = Todo.query.get(id)

    try:
        #Attempt to delete object
        db.session.delete(task_to_delete)
         #commiting to database
        db.session.commit()
        #Using redirect to redirect user to homepage
        return redirect('/')
    except: 
        return "Error detected: Task could not be deleted from database"   


#Method to delete object
@app.route('/update/<int:id>' ,methods=['GET', 'POST'])
#Takes in id para
def update(id):
    #This will query the DB 
    task_to_updatee = Todo.query.get(id)

    #If method is post the todo will be added to the database
    if request.method == 'POST':
      #Setting the data from the content box to the actual task
        task_to_updatee.content = request.form['content']

        try:
            db.session.commit()
            #redirect the user to the homepage
            return redirect("/")
        except:
            return "There was an issue updating the task"

    else:
        return render_template('update.html' , task = task_to_updatee)


if __name__ == "__main__":
    #Debug set to true to indicate any errors
    #app.run starts the web server
    app.run(debug=True)

