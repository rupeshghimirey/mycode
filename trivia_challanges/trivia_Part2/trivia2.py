#!/usr/bin/python3
from flask import Flask,request,session
from flask import redirect
from flask import render_template
import questions

# create flask app instance    
app = Flask(__name__)
app.secret_key = "viaanRaj"

# variables that can be passed through render_template
user_name = "Rupesh"
question_answer_dict = questions.question_and_answer()
question= question_answer_dict["question"]
answer= question_answer_dict["answer"]

print(question)
print(answer)

@app.route("/")
def home():
    return render_template('trivia.html',name=user_name, question_answer_dict = question_answer_dict, answer=answer,)

@app.route("/incorrect")
def incorrect():
    return render_template('incorrect.html')

@app.route("/correct")
def correct():
    trivia_answer_option = session['user_input']
    print(trivia_answer_option)
    return render_template('correct.html',name=user_name, question_answer_dict = question_answer_dict, answer=answer,trivia_answer_option=trivia_answer_option)

@app.route("/trivia", methods=["POST"])
def correct_answer():
    trivia_answer_option = request.form['answer']
    session['user_input'] = trivia_answer_option
    if(question_answer_dict[trivia_answer_option].upper() == answer.upper()):
        return redirect("/correct")
    else:
        return redirect("/correct")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)