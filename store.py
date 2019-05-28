meals = []
orders = []


class Meal :
    def __init__(self, id, name, description, price, image):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.image = image


class Order :
    def __init__(self, id, meal, customer_name, customer_address):
        self.id = id
        self.meal = meal
        self.customer_name = customer_name
        self.customer_address = customer_address

class MealStore:
    def get_all(self):
        return meals

    def add(self, meal):
        meals.append(meal)

    def get_by_id(self, id):
        result = None
        for meal in meals:
            if meal.id == id:
                result = meal
                break
        return result

    def update(self,id,fields):
        meal = self.get_by_id(id)
        meal.name = fields["name"]
        meal.description = fields["description"]
        meal.image =fields["image"]
        meal.price =fields["price"]
        return meal

    def delete(self,id):
        meal = self.get_by_id(id)
        meals.remove(meal)
        return meals


class OrderStore:
    def get_all(self):
        return orders

    def add(self, Order):
        orders.append(Order)

    def get_by_id(self, id):
        result = None
        for order in orders:
            if order.id == id:
                result = order
                break
        return result