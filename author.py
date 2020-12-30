from flask import Flask,render_template
app=Flask(__name__)
authors=("asdasd","sdas","asdasd")
@app.route('/tabledf')
def good():
    return render_template("tabledf.html", authors=authors)
if __name__=="__main__":
    app.run(debug=True)
