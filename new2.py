from flask import Flask
app=Flask(__name__)
@app.route('/')
def new():
    return "good evening"

@app.route('/morning')
def new1():
    return "good morning"

@app.route('/night')
def new2():
    return "good night"

@app.route('/data')
def new4():
    return  "<html> <table><td><p>my name is akshay sdakljsd</p><h1> jhad sdkhasd djkas</h1></td></table></html>"


if __name__=="__main__":
    app.run(debug="True")
    


             
