#Importing functions from flask
from flask import Flask, render_template , url_for

#Instantaiting application referencing the file 
app = Flask(__name__)

#Creating index route
@app.route("/")
def index():
    return render_template('index.html')

if __name__ == "__main__":
    #Debug set to true to indicate any errors
    #app.run starts the web server
    app.run(debug=True)