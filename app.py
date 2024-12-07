from flask import Flask , render_template

# The first argument is the name of the application's module or package 
# __name__ is a convenient way to get the name of the current module
app= Flask(__name__)
# Define the route for the root URL ('/') 
# When a user visits the root URL, the hello_world() function will be called
@app.route('/')
def hello_world():
    return render_template('index.html')

 