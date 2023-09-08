from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Food:
    def __init__(self, data):
        self.id = data['id']
        self.name_group = data['name_group']
        self.name = data['name']
        self.food_id = data['food_id']
        self.value= data['value']
       

    @classmethod
    def vegetables(cls):
        query = "SELECT  food_type.id ,food_type.name_group , food.name, food.idfood_groups  as food_id, food.value FROM food_type JOIN food ON food_type.id=food.food_type_id WHERE  food_type.id = 1;"
        results= connectToMySQL('proyect_db').query_db(query)
        vegetables=[]
        for vegetable in results:
            vegetables.append(cls(vegetable))
        return vegetables
    
    @classmethod
    def fruits(cls):
        query = "SELECT  food_type.id ,food_type.name_group , food.name, food.idfood_groups  as food_id, food.value FROM food_type JOIN food ON food_type.id=food.food_type_id WHERE  food_type.id = 2;"
        results= connectToMySQL('proyect_db').query_db(query)
        fruits=[]
        for fruit in results:
            fruits.append(cls(fruit))
        return fruits
    

    @classmethod
    def grains(cls):
        query = "SELECT  food_type.id ,food_type.name_group , food.name, food.idfood_groups  as food_id, food.value FROM food_type JOIN food ON food_type.id=food.food_type_id WHERE  food_type.id = 3;"
        results= connectToMySQL('proyect_db').query_db(query)
        grains=[]
        for grain in results:
            grains.append(cls(grain))
        return grains

    @classmethod
    def protein(cls):
        query = "SELECT  food_type.id ,food_type.name_group , food.name, food.idfood_groups  as food_id, food.value FROM food_type JOIN food ON food_type.id=food.food_type_id WHERE  food_type.id = 4;"
        results= connectToMySQL('proyect_db').query_db(query)
        proteins=[]
        for protein in results:
            proteins.append(cls(protein))
        return proteins
    
    @classmethod
    def fats(cls):
        query = "SELECT  food_type.id ,food_type.name_group , food.name, food.idfood_groups  as food_id, food.value FROM food_type JOIN food ON food_type.id=food.food_type_id WHERE  food_type.id = 5;"
        results= connectToMySQL('proyect_db').query_db(query)
        fats=[]
        for fat in results:
            fats.append(cls(fat))
        return fats



    @classmethod
    def savemenub(cls,data):
        query = "INSERT INTO menu (count,created_at,user_id,meals_id,food_id) VALUES (%(qvb)s,now(),%(userId)s,1,%(vegetable_b)s), (%(qfb)s,now(),%(userId)s,1,%(fruit_b)s), (%(qgb)s,now(),%(userId)s,1,%(grain_b)s),(%(qpb)s,now(),%(userId)s,1,%(protein_b)s),(%(qfab)s,now(),%(userId)s,1,%(fat_b)s);"
        results= connectToMySQL('proyect_db').query_db(query,data)
        return
    
    @classmethod
    def savemenul(cls,data):
        query = "INSERT INTO menu (count,created_at,user_id,meals_id,food_id) VALUES (%(qvl)s,now(),%(userId)s,2,%(vegetable_l)s), (%(qfl)s,now(),%(userId)s,2,%(fruit_l)s), (%(qgl)s,now(),%(userId)s,2,%(grain_l)s),(%(qpl)s,now(),%(userId)s,2,%(protein_l)s),(%(qfal)s,now(),%(userId)s,2,%(fat_l)s);"
        results= connectToMySQL('proyect_db').query_db(query, data)
        return
    
    @classmethod
    def savemenus(cls,data):
        query = "INSERT INTO menu (count,created_at,user_id,meals_id,food_id) VALUES (%(qvs)s,now(),%(userId)s,3,%(vegetable_s)s), (%(qfs)s,now(),%(userId)s,3,%(fruit_s)s), (%(qgs)s,now(),%(userId)s,3,%(grain_s)s),(%(qps)s,now(),%(userId)s,3,%(protein_s)s),(%(qfas)s,now(),%(userId)s,3,%(fat_s)s);"
        results= connectToMySQL('proyect_db').query_db(query, data)
        return
    
    @classmethod
    def savemenud(cls,data):
        query = "INSERT INTO menu (count,created_at,user_id,meals_id,food_id) VALUES (%(qvd)s,now(),%(userId)s,4,%(vegetable_d)s), (%(qfd)s,now(),%(userId)s,4,%(fruit_d)s), (%(qgd)s,now(),%(userId)s,4,%(grain_d)s),(%(qpd)s,now(),%(userId)s,4,%(protein_d)s),(%(qfad)s,now(),%(userId)s,4,%(fat_d)s);"
        results= connectToMySQL('proyect_db').query_db(query,data)
        return