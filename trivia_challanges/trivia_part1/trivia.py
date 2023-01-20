#!/usr/bin/python3
from flask import Flask,request,session
from flask import redirect,render_template



# create flask app instance    
app = Flask(__name__)

@app.route("/")
def home():
    user_name = session.get("user_name")
    return render_template('trivia.html', user_name=user_name)

@app.route("/correct")
def correct():

    return render_template('correct.html')

@app.route("/trivia", methods=["POST"])
def correct_answer():
    
    trivia_answer = int(request.form['answer'])
    if(trivia_answer == 7):
        return redirect("/correct")
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
