from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash


class Weight:
    def __init__(self, data):
        self.id = data['id']
        self.energy = data['energy']
        self.weight = data['weight']
        self.goal_w = data['goal_w']
        self.arm= data['arm']
        self.hip= data['hip']
        self.weist= data['weist']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @staticmethod
    def validate_values(data):
        is_valid = True
        if len(data['energy']) == 0 :
            flash("must ned  the  Energy value")
            is_valid = False
        if len(data['weight']) == 0 :
            flash("must ned  the Weight value")
            is_valid = False
        if len(data['goal_w']) == 0 :
            flash("must ned  the Goal Weight value")
            is_valid = False
        if len(data['arm']) == 0 :
            flash("must ned  the arm measure ")
            is_valid = False
        if len(data['hip']) == 0 :
            flash("must ned  the hip measure ")
            is_valid = False
        if len(data['waist']) == 0 :
            flash("must ned  the waist measure")
            is_valid = False
        return is_valid

    @classmethod
    def savewvalues(cls, data):
        query = "INSERT INTO w_info  (energy, weight , goal_w , arm ,hip,weist, created_at, updated_at, user_id)  VALUES ( %(energy)s, %(weight)s , %(goal_w)s , %(arm)s, %(hip)s, %(weist)s,now(), now(), %(user_id)s)"
        # los nombres deben ser los de la bd / los valores los del html
        new_w_id=connectToMySQL('proyect_db').query_db(query, data)
        return new_w_id
    

