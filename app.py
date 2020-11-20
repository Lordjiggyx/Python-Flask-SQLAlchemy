#Importing flask
from flask import Flask

#Instantaiting application referencing the file 
app = Flask(__name__)

#Creating index route
@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    #Debug set to true to indicate any errors
    #app.run starts the web server
    app.run(debug=True)