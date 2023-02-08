from flask import Blueprint, render_template, request, flash 
import random
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Flask Settings
LISTEN_ALL = "0.0.0.0"
FLASK_IP = LISTEN_ALL
FLASK_PORT = 81
FLASK_DEBUG = True

app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html")

@app.route('/', methods=['GET','POST'])
def home():
    return render_template("student-attendence.html")

@app.route('/teacher-portal', methods=['GET','POST'])
def techerPortal():
    return render_template("teacher-portal.html")


def get_value():
    low = 100000
    high = 999999
    num = random.randint(low, high)
    value = num
    print (value)
    return value

@app.route('/random-code-generator', methods=['GET','POST'])
def randomCodeGenerator():
    value_generator = ""
    if request.method == 'POST':
        value_generator = get_value()
    return render_template("random-code-generator.html", value_generator=value_generator)



# @app.route("/get_value", methods=["POST"])
def get_value():
    low = 0
    high = 999999
    num = random.randint(low, high)
    value = num
    print (value)
    return value

# @app.route('/student-attendence', methods=['GET','POST'])
# def studentAttendence():
#     value_generator = ""
#     if request.method == 'POST':
#         value_generator = get_value()
#     #low = 0
#     #high = 999999
#     #num = random.randint(low, high)
#     # if form.validate_on_submit():
#     #x = ("Jouw unieke aanwezigheids code voor vandaag is:" + str(num))
    
#     return render_template("student-attendence.html", value_generator=value_generator)

    

@app.route('/logout')
def logout():
    return "<p>Logout</p>"

@app.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email= request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(email) < 5:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(firstName) < 3:
            flash('First name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Password don\'t match.', category='error')
        elif len(password1) < 8:
            flash('Password must be at least 8 characters', category='error')
        else: 
            flash('Account created', category='succes')
            pass
    return render_template("sign_up.html")

if __name__ == '__main__':
     app.run(debug=True)