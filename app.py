
#This is the app with out css: 

#from flask import Flask
#
#app= Flask(__name__)
#
#@app.route('/')
#def hello_world():
#    return 'Hello this is Flask App answering!'




from flask import Flask , render_template #render template manages the html and the css files with flask

# The first argument is the name of the application's module or package 
# __name__ is a convenient way to get the name of the current module
app= Flask(__name__)
# Define the route for the root URL ('/') 
# When a user visits the root URL, the hello_world() function will be called
@app.route('/')
def hello_world():
    return render_template('index.html')

# Jinja2 handles the logic for rendering the index.html template
# Flask serves the CSS styles from the static folder


 

