
from cgi import print_form
from crypt import methods
import re
from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.menu import Menu
from flask_app.models.user import User
# from flask_app.models.recipes import Recipes
# from flask_app.models.recipeonly import Recipes_only
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import flash

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/patient")
def doctor():
    return render_template("patientlg.html") 

@app.route("/doctor")
def patient():
    return render_template("doctorlg.html") 



@app.route("/register/doctor", methods=["POST"])
def register():   
    if not User. validate_doctor(request.form): # is la validacion es falso mandamos a index
        return redirect('/doctor')
    pw_hash = bcrypt.generate_password_hash(request.form['password']) # crear Hash del password
    print(pw_hash)

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
    } 
    # print(request.form)
    this_user = User.find_the_email(data)
    if  this_user: # if the query return  o == falrse
        flash("email is already use!")
        return redirect("/doctor")


    use_id= User.savedoctor(data)
    session['logged_id'] = use_id
    return redirect("/success")


@app.route("/success")
def success():
    if"logged_id" not in session:
        return redirect("/doctor")
    data ={
        "id" : session['logged_id']
    }
    loged_user= User.user_by_id(data)

    patients = User.get_all_patients()


    # return f"you are logged in as user # {session['logged_id']} !"
    return render_template("allpatients.html",loged_user=loged_user,patients=patients)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

#----------------------------------------------------registration dr

@app.route('/login_doctor', methods=["POST"])
def login_doctor():
    data ={
        "email" : request.form["email"]
    }
    this_user = User.find_the_email(data)
    if not this_user: # if the query return  o == falrse
        flash("invalid email/password")
        return redirect("/doctor")
    #if user exist
    if not bcrypt.check_password_hash(this_user.password, request.form['password']):
        flash("password is wrong")
        return redirect("/doctor")
    #-chec and cpompare the password

    session['logged_id']= this_user.id
 
    return redirect("/success")

#----------------------------------------------------loggin dr

#----------------------------------------------------loggin 

@app.route("/register/patient", methods=["POST"])
def register_patient():   
    if not User.validate_patient(request.form): # is la validacion es falso mandamos a index
        return redirect('/patient')
    pw_hash = bcrypt.generate_password_hash(request.form['password']) # crear Hash del password
    print(pw_hash)

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "age": int(request.form["age"]),
        "height": float(request.form["height"]),
        "initial_weight": float(request.form["initial_weight"]),
        "password": pw_hash
    } 
    # print(request.form)
    this_user = User.find_the_email(data)
    if  this_user: # if the query return  o == falrse
        flash("email is already use!")
        return redirect("/patient")


    use_id= User.savepatient(data)
    session['logged_id'] = use_id
    return redirect("/successp")


@app.route("/successp")
def successp():
    if"logged_id" not in session:
        return redirect("/patient")
    data = {
        "userId" : session['logged_id'],
        "timeId": 1
    }

    breakfast_list = Menu.get_menu_by_time(data)

    data = {
        "userId" : session['logged_id'],
        "timeId": 2
    }
    lunch_list = Menu.get_menu_by_time(data)

    data = {
        "userId" : session['logged_id'],
        "timeId": 3
    }
    snack_list = Menu.get_menu_by_time(data)

    data = {
        "userId" : session['logged_id'],
        "timeId": 4
    }
    dinner_list = Menu.get_menu_by_time(data)
    
    return render_template("showmenu.html", breakfast_list=breakfast_list, lunch_list=lunch_list, snack_list=snack_list, dinner_list=dinner_list)

@app.route('/login_patient', methods=["POST"])
def login_patient():
    data ={
        "email" : request.form["email"]
    }
    this_user = User.find_the_email(data)
    if not this_user: # if the query return  o == falrse
        flash("invalid email/password")
        return redirect("/patient")
    #if user exist
    if not bcrypt.check_password_hash(this_user.password, request.form['password']):
        flash("password is wrong")
        return redirect("/patient")
    #-chec and cpompare the password

    session['logged_id']= this_user.id
 
    return redirect("/successp")

#----------------------------------------------------loggin dr

