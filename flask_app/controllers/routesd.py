from crypt import methods
import re
from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.controllers.routes import patient
from flask_app.models.user import User
from flask_app.models.w import Weight
from flask_app.models.food import Food
# from flask_app.models.recipeonly import Recipes_only
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import flash


@app.route('/edit_values/<int:id>')
def edit_values(id):
    return render_template("patientvalues.html", patientId=id)


@app.route('/edit_values/patient/<int:id>', methods=["POST"])
def edit_valuesd(id):
    if"logged_id" not in session:
        return redirect("/patient")

    print(id)
    if not Weight.validate_values(request.form): # is la validacion es falso mandamos a index
        return redirect('/edit_values/' + str(id))
    data = {
        "energy": int(request.form["energy"]),
        "weight": float(request.form["weight"]),
        "goal_w": float(request.form["goal_w"]),
        "arm": float(request.form["arm"]),
        "hip": float(request.form["hip"]),
        "weist": float(request.form["waist"]),
        "user_id": id
        } 

    new=Weight.savewvalues(data)

    return redirect("/")


@app.route('/edit_menu')
def edit_menu():
    vegetables=Food.vegetables()
    fruits=Food.fruits()
    grains=Food.grains()
    protein=Food.protein()
    fats=Food.fats()
    # for v in vegetables:
    #     print(v.name)
    
    return render_template("editmenu.html",vegetables=vegetables,fruits=fruits,grains=grains,proteins=protein,fats=fats)

@app.route('/save_menu',methods=["POST"])
def save_menu():
    if"logged_id" not in session:
        return redirect("/patient")

    print("save_menu")
    print("Breakfaste veggie")
    print(request.form)

    datab = {
        "userId" : session['logged_id'],
        "vegetable_b" : request.form['vegetable_b'],
        "qvb":int(request.form['qvb']),
        "fruit_b": request.form['fruit_b'],
        "qfb":int(request.form['qfb']),
        "grain_b": request.form['grain_b'],
        "qgb":int(request.form['qgb']),
        "protein_b": request.form['protein_b'],
        "qpb":int(request.form['qpb']),
        "fat_b": request.form['fat_b'],
        "qfab":int(request.form['qfab'])
    }
    datal = {
        "userId" : session['logged_id'],
        "vegetable_l": request.form['vegetable_l'],
        "qvl":int(request.form['qvl']),
        "fruit_l": request.form['fruit_l'],
        "qfl":int(request.form['qfl']),
        "grain_l": request.form['grain_l'],
        "qgl":int(request.form['qgl']),
        "protein_l": request.form['protein_l'],
        "qpl":int(request.form['qpl']),
        "fat_l": request.form['fat_l'],
        "qfal":int(request.form['qfal'])
    }
    datas = {
        "userId" : session['logged_id'],
        "vegetable_s": request.form['vegetable_s'],
        "qvs":int(request.form['qvs']),
        "fruit_s": request.form['fruit_s'],
        "qfs":int(request.form['qfs']),
        "grain_s": request.form['grain_s'],
        "qgs":int(request.form['qgs']),
        "protein_s": request.form['protein_s'],
        "qps":int(request.form['qps']),
        "fat_s": request.form['fat_s'],
        "qfas":int(request.form['qfas'])
    }
    datad = {
        "userId" : session['logged_id'],
        "vegetable_d" : request.form['vegetable_d'],
        "qvd":int(request.form['qvd']),
        "fruit_d": request.form['fruit_d'],
        "qfd":int(request.form['qfd']),
        "grain_d": request.form['grain_d'],
        "qgd":int(request.form['qgd']),
        "protein_d": request.form['protein_d'],
        "qpd":int(request.form['qpd']),
        "fat_d": request.form['fat_d'],
        "qfad":int(request.form['qfad'])

    }

    Food.savemenub(datab)
    Food.savemenul(datal)
    Food.savemenus(datas)
    Food.savemenud(datad)

    return redirect("/successp")





    # datab = {
    #     "vegetable_b" : request.form['vegetable_b'],
    #     "qvb":request.form['qvb'],
    #     "fruit_b": request.form['fruit_b'],
    #     "qfb":request.form['qfb'],
    #     "graib_b": request.form['graib_b'],
    #     "qgb":request.form['qgb'],
    #     "protein_b": request.form['protein_b'],
    #     "qpb":request.form['qpb'],
    #     "fat_b": request.form['fat_b'],
    #     "qfab":request.form['qfab']
    # }
    # datal = {
    #     "vegetable_l": request.form['vegetable_l'],
    #     "qvl":request.form['qvl'],
    #     "fruit_l": request.form['fruit_l'],
    #     "qfl":request.form['qfl'],
    #     "grain_l": request.form['grain_l'],
    #     "qgl":request.form['qgl'],
    #     "protein_l": request.form['protein_l'],
    #     "qpl":request.form['qpl'],
    #     "fat_l": request.form['fat_l'],
    #     "qfal":request.form['qfal']
    # }
    # datas = {
    #     "veggetable_s": request.form['vegetable_s'],
    #     "qvs":request.form['qvs'],
    #     "fruit_s": request.form['fruit_s'],
    #     "qfs":request.form['qfs'],
    #     "grain_s": request.form['grain_s'],
    #     "qgs":request.form['qgs'],
    #     "protein_s": request.form['protein_s'],
    #     "qps":request.form['qps'],
    #     "fat_s": request.form['fat_s'],
    #     "qfas":request.form['qfas']
    # }
    # datad = {
    #     "vegetable_d" : request.form['vegetable_d'],
    #     "qvd":request.form['qvd'],
    #     "fruit_d": request.form['fruit_d'],
    #     "qfd":request.form['qfd'],
    #     "grain_d": request.form['grain_d'],
    #     "qgd":request.form['qgd'],
    #     "protein_d": request.form['protein_d'],
    #     "qpd":request.form['qpd'],
    #     "fat_d": request.form['fat_d'],
    #     "qfad":request.form['qfad']

    # }