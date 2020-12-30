from flask import *

app=Flask(__name__)
@app.route('/',methods=["post"])
def new():
    email=request.post["email"]
    return "%s" %email
if __name__=='__main__':
    app.run(debug=True)

    
