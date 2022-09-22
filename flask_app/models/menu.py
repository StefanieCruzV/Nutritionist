from flask_app.config.mysqlconnection import connectToMySQL

class Menu:
    def __init__(self, data):
        self.name = data['name']
        self.count = data['count']
        self.time = data['time']
        self.type = data['type']
    
    @classmethod
    def get_menu_by_time(cls, data):
        query = "SELECT food.name , user.first_name , menu.count ,meals.time, user.id as userId, menu.created_at, food_type.name_group as type  FROM menu JOIN food ON  menu.food_id=food.idfood_groups JOIN food_type on food.food_type_id = food_type.id JOIN meals ON menu.meals_id=meals.int JOIN user ON menu.user_id=user.id WHERE  user.id = %(userId)s AND meals.int = %(timeId)s  ORDER BY menu.created_at DESC LIMIT 5;"
        results= connectToMySQL('proyect_db').query_db(query, data)
        print(results)
        menu_list=[]
        for menu in results:
            menu_list.append(cls(menu))
        return menu_list


    

        {% if not dinner_list%}
        <td class="text-center"> <span>0</span></td>
        <td><input type="number" value="0"></td>
        {% else %}
        <td class="text-center"> <span>{{dinner_list[0].name}}</span></td>
        <td><input type="number" value={{dinner_list[2].count}}></td>
        {%endif%}
