from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
NAME =re.compile(r'^[a-zA-Z ]+$' )
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NUMS= re.compile(r'^[0-9.]+$')



class User:
    def __init__(self, data):
        self.id = data['id']
        self.type = data['type']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email= data['email']
        self.age= data['age']
        self.height= data['height']
        self.initial_weight= data['initial_weight']
        self.password= data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        


    @staticmethod
    def validate_doctor(data):
        is_valid = True
        if not NAME.match(data['first_name']):
            flash("Name must be only characters.")
            is_valid = False
        if  len(data['first_name']) < 2:
            flash("Name must be at least 2 .")
            is_valid = False
        if not NAME.match(data['last_name']):
            flash("Last name must be only characters.")
            is_valid = False
        if  len(data['first_name']) < 2:
            flash("Last ame must be at least 2 .")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!")
            is_valid = False
        if len(data['password']) == 0 :
            flash("must ned the password")
            is_valid = False
        if len(data['confirmpassword']) == 0:
            flash("must ned the confirmation")
            is_valid = False
        if data['password'] != data['confirmpassword']:
            flash("Confirmation must match the password")
            is_valid = False
        return is_valid



    @staticmethod
    def validate_patient(data):
        is_valid = True
        if not NAME.match(data['first_name']):
            flash("Name must be only characters.")
            is_valid = False
        if  len(data['first_name']) < 2:
            flash("Name must be at least 2 .")
            is_valid = False
        if not NAME.match(data['last_name']):
            flash("Last name must be only characters.")
            is_valid = False
        if  len(data['first_name']) < 2:
            flash("Last ame must be at least 2 .")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!")
            is_valid = False
        if len(data['height']) == 0 :
            flash("must ned the height")
            is_valid = False
        if not NUMS.match(data['height']):
            flash("Invalid email height!")
            is_valid = False
        if len(data['initial_weight']) == 0 :
            flash("must ned the Weight")
            is_valid = False
        if not NUMS.match(data['initial_weight']):
            flash("Invalid email Weight!")
            is_valid = False
        if not NUMS.match(data['age']):
            flash("Invalid email age!")
            is_valid = False
        if len(data['age']) == 0 :
            flash("must ned the age")
            is_valid = False
        if len(data['password']) == 0 :
            flash("must ned the password")
            is_valid = False
        if len(data['confirmpassword']) == 0:
            flash("must ned the confirmation")
            is_valid = False
        if data['password'] != data['confirmpassword']:
            flash("Confirmation must match the password")
            is_valid = False
        return is_valid

    @classmethod
    def savepatient(cls, data):
        query = "INSERT INTO user (type, first_name , last_name , email ,age,height,initial_weight, password, created_at, updated_at)  VALUES (1, %(first_name)s , %(last_name)s , %(email)s, %(age)s,%(height)s,%(initial_weight)s, %(password)s, now(), now())"
        # los nombres deben ser los de la bd / los valores los del html
        new_user_id=connectToMySQL('proyect_db').query_db(query, data)
        return new_user_id

    @classmethod
    def savedoctor(cls, data):
        query = " INSERT INTO user (type, first_name , last_name , email , password, created_at, updated_at)   VALUES ( 2, %(first_name)s , %(last_name)s , %(email)s, %(password)s, now(), now())"
        # los nombres deben ser los de la bd / los valores los del html
        new_user_id=connectToMySQL('proyect_db').query_db(query, data)
        return new_user_id
    
    @classmethod
    def find_the_email(cls, data):
        query = "SELECT * FROM user WHERE email = %(email)s"
        # los nombres deben ser los de la bd / los valores los del html
        result= connectToMySQL('proyect_db').query_db(query, data)
        print("-------")
        print(result)
        if len(result) == 0: #si no esta ese email
            return False 
        email = cls(result[0]) 
        return email

    @classmethod
    def user_by_id(cls, data):
        query = "SELECT * FROM user WHERE id = %(id)s"
        # los nombres deben ser los de la bd / los valores los del html
        result= connectToMySQL('proyect_db').query_db(query, data)
        if len(result) == 0: #si no esta ese email
            return False 
        user = cls(result[0]) 
        return user


  
    @classmethod
    def get_all_patients(cls):
        query = "SELECT * from user where type = 1"
        results = connectToMySQL('proyect_db').query_db(query)
        print(results)
        patients = []
        # crea arreglo para guiardar los valores 
        for patient in results: #itera los nombres de la base de datos 
            data = {
                "id" : patient["id"],
                "first_name" : patient["first_name"],
                "last_name" : patient["last_name"],
                "age" : patient["age"],
                "height" : patient["height"],
                "initial_weight" : patient["initial_weight"]
                }
            patients.append(cls(patient))
        
            # flos mete en el arreglo -y los convierte en una clkase ususario
        return patients








