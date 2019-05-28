from flask import Flask, render_template, request, url_for, redirect
from store import Meal, Order, MealStore, OrderStore

app = Flask(__name__)

meal1 = Meal(id=1, name= 'Burgar', description= 'With Slices Of Meat & Cheese' , price= '15' ,
          image='https://5.imimg.com/data5/PQ/XG/GLADMIN-58136472/veg-burger-500x500.png' )
meal2 = Meal(id=2, name= 'Grilled chicken', description= 'With Avocado & Lettuce' , price= '30' ,
          image= 'https://academy-discorce-s3.s3.dualstack.us-east-2.amazonaws.com/upload/original/2X/f/f3c39987ea00d4d186f6f0d41d9aa5f274190fd9.jpeg')
meal3 = Meal(id=3, name= 'Steak', description= 'With Fresh Vegetables & Juice' , price= '35' ,
          image='https://academy-discorce-s3.s3.dualstack.us-east-2.amazonaws.com/upload/original/2X/3/31b44ea15e8a14895fd9383e7845fd7a1bc96838.jpeg' )
meal4 = Meal(id=4, name= 'Potato With Bechamel', description= 'With Spices & Herbs' , price= '20' ,
           image='https://academy-discorce-s3.s3.dualstack.us-east-2.amazonaws.com/upload/original/2X/0/04274034174fb71006e950b05292abc3934f9f1e.jpeg' )

order1 = Order(id=1, meal= meal1 , customer_name='Bayan Radaideh', customer_address= 'Amman')
order2 = Order(id=2, meal= meal2, customer_name='Bayan Radaideh' , customer_address= 'Amman')
order3 = Order(id=3, meal= meal3 , customer_name='Bayan Radaideh' , customer_address= 'Amman')

meal_store = MealStore()
meal_store.add(meal1)
meal_store.add(meal2)
meal_store.add(meal3)
meal_store.add(meal4)
app.current_meal_id = 5

order_store = OrderStore()
order_store.add(order1)
order_store.add(order2)
order_store.add(order3)
app.current_order_id = 4



@app.route('/')
def home():
    return render_template('user-list-meals.html', meals = meal_store.get_all())

@app.route('/fill-order/<int:id>', methods=['GET', 'POST'])
def fill_order(id):
    if request.method=='POST':
        meal = meal_store.get_by_id(id)
        new_order = Order(id=app.current_order_id,
                    meal = meal,
                    customer_name=request.form['customer_name'],
                    customer_address=request.form['customer_address'])
        order_store.add(new_order)
        app.current_order_id += 1

        return redirect(url_for('admin_meals'))
    else:
        return render_template('user-fill-order.html')



@app.route('/admin/orders/')
def admin_orders():
    return render_template('admin-orders.html', orders=order_store.get_all())

@app.route('/admin/meals/')
def admin_meals():
    return render_template('admin-meals.html', meals=meal_store.get_all())

@app.route('/admin/meals/add', methods=['GET', 'POST'])
def admin_add_meal():
    if request.method=='POST':
        new_meal = Meal(id=app.current_meal_id,
                    name=request.form['name'],
                    description=request.form['description'],
                    price=request.form['price'],
                    image=request.form['image'])
        meal_store.add(new_meal)
        app.current_meal_id += 1
        return redirect(url_for('admin_meals'))
    else:
        return render_template('admin-add-meal.html')

@app.route('/admin/meals/edit/<int:id>', methods=['GET', 'POST'])
def admin_edit_meal(id):
    if request.method == 'POST':
        name=request.form['name']
        description=request.form['description']
        price=request.form['price']
        image=request.form['image']
        meal_store.update(id, {'name': name, 'description': description, 'price': price, 'image': image})
        return redirect(url_for('admin_meals'))

    elif request.method == 'GET':
        meal = meal_store.get_by_id(id)
        return render_template('admin-edit-meal.html', meal=meal)

    return render_template('admin-meals.html', meals=meal_store.get_all())

@app.route('/admin/meals/delete/<int:id>')
def admin_delete_meal(id):
    meal_store.delete(id)
    return redirect(url_for('admin_meals'))