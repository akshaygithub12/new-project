from flask import Flask
app=Flask(__name__)
@app.route('/<string:name>/<int:age>')
def good(name,age):
    return "hello " +name +"age"+str(age)

if __name__=="__main__":
    app.run(debug=True)
