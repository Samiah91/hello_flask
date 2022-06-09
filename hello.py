from flask import Flask

app = Flask(__name__)    
@app.route('/')          
def index():
    return 'Hello World!'     

@app.route('/dojo')          
def dojo():
    return 'dojo'

@app.route('/say/<name>')          
def say(name):
    return f'hi{name}' 

@app.route('/repeat/<num>/<name>')          
def repeat(num,name):
    return f'hi{name} ' * int(num)



if __name__=="__main__":       
    app.run(debug=True)    