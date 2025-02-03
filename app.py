#
 
from flask import Flask
from flask import render_template,request
import textblob
import google.generativeai as gen_ai

import os
api =os.getenv('makersuite') #omit if hardcoded in genai_result function
api = 'AIzaSyCmQpUmyFbGn9gbi61v22PS6OI8Fn4DYTk'


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    name = request.form.get("q")
    return(render_template("main.html"))

@app.route("/SA",methods=["GET","POST"])
def SA():
    return(render_template("SA.html"))

@app.route("/SA_result",methods=["GET","POST"])
def SA_result():
    q = request.form.get('q')
    r = textblob.TextBlob(q).sentiment
    return(render_template("SA_result.html", r=r))

@app.route("/genai",methods=["GET","POST"])
def genai():
    return(render_template("genai.html"))

@app.route("/genai_result", methods=["GET", "POST"])
def genai_result():
    q = request.form.get('q')
    gen_ai.configure(api_key=api) #hard code api key directly api_key = xxx
    model=gen_ai.GenerativeModel('gemini-1.5-flash')
    r = model.generate_content(q)
    r =r.text
    return render_template("genai_result.html", r = r)

@app.route("/paynow",methods=["GET","POST"])
def paynow():
    return(render_template("paynow.html"))

if __name__ == "__main__":

    app.run(port=1111)






