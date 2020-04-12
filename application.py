from flask import Flask, render_template, request #ovde smo dodali i requeast trebaće nam za form

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST"]) #ovde je metod post, po defoltu je GET, tako da aplikacija očekuje da korisnik nešto preda
def hello():
    name = request.form.get("name").capitalize() #ovde taj form iz indeksa predaj evrednost u name na kraju sam ga povećao
    surname =request.form.get("surname").capitalize() #ovde sam se pravio malo važan i ubacio sam i promenljivu prezime
    return render_template("hello.html", name=name, surname=surname) #tu promenljivu predaje u name i upućuje u hello.html
