from config import *
from bottle import *
from entities import *
from pony.orm.integration.bottle_plugin import PonyPlugin
install(PonyPlugin())
import datetime

#########Any method that takes an argument needs to be
####within a catch block to catch errors if cannot find entity looking for

'''
    Server module
    =============
    This module provides all the basic functionalities of the application.
    The module is a standard Bottle application and runs on port 8080.
'''

'''
    Home page of application
'''
@route('/')
def index():
    return template('index')

#######################################
########    Brand functions   #########
#######################################
'''
    Index page for the brands
'''
@route('/brands')
def all_brands():
    # select all the students from the db
    brands = select(b for b in Brand)
    # render the list using the students/index template.
    return template('brands/index', brands = brands)
'''
    Displays brand info, i.e name, nationality.
'''
@route('/brands/<id>/')
def show_brand(id):
    # fetch brand from database
    brand = Brand[id]
    #return template to show brand info to screen
    return template('brands/show', brand = brand)

'''
    Form to edit brand info
'''
@route('/brands/<id>/edit')
def edit_brand(id):
    # fetch brand from database
    brand = Brand[id]
    #show form to user via template
    return template('brands/edit', brand = brand)

'''
   Edit a brand based on input acquired from form
'''
@route('/brands/<id>/edit', method='POST')
def update_brands(id):
    # fetch brand from database
    brand = Brand[id]
    # update the brand name
    brand.name = request.forms.get('name')
    # update the brand nationality
    brand.nation = request.forms.get('nation')
    # redirect to the brand-specific info page
    redirect("/brands/%s/" % id)

'''
    shows form to add a brand to the screen
'''
@route('/brands/add')
def add_brand():
    # show form using template
    return template('brands/add')

'''
    Uses information from the add form to create a new brand
'''
@route('/brands/add', method='POST')
def new_brand():
    name = request.forms.get('name')
    nation = request.forms.get('nation')
    Brand(name = name, nation = nation)
    redirect("/brands")

'''
    Delete brand after getting its id via form action
'''
@route('/brands/<id>/delete', method='POST')
def delete_brand(id):
    brand = Brand[id]
    brand.delete()
    redirect('/brands')

'''
search for brand by name, if nothing found, return empty list
'''
@route('/brands/search', method='POST')
def find_brand():
    try:
        key = request.forms.get('key')
        brands = Brand.select(lambda b: b.name==str(key))
        if len(brands)!=0:
            return template('brands/search', brands=brands)
        brands = Brand.select(lambda b: b.nation==str(key))
        if len(brands)!= 0:
            return template('brands/search', brands=brands)
        brands  = []
        return template('brands/search', brands=brands)
    except Exception:
        brands = []
        return template('brands/search', brands=brands)


#######################################
########     Car functions   ##########
#######################################
'''
list all cars 
'''

@route('/cars')
def all_cars():
    # retrieving all the courses from the db
    cars = select(c for c in Car)
    # render the index page for courses
    return template('cars/index', cars = cars)

'''
    Returns page showing info on specific car.
'''
@route('/cars/<id>/')
def show_car(id):
    # retrieve the student by id from the database
    car = Car[id]
    # render the info using the show template for students
    return template('cars/show', car = car)

'''
    Form to edit car info.
'''
@route('/cars/<id>/edit')
def edit_student(id):
    # retrieve the student by id from the database
    car = Car[id]
    brands = Brand.select()
    # render the form using the edit template for students
    return template('cars/edit', car = car, brands = brands)
'''
Uses info from edit car form to edit attributes of specific Student in db
'''
@route('/cars/<id>/edit', method='POST')
def update_car(id):
    try:
        # retrieve the car by id from the database
        car = Car[id]
        # updating the brand, model, price and availability
        brand = Brand.get(lambda b: b.name == request.forms.get('brand'))
        car.brand = brand
        car.model = request.forms.get('model')
        car.price = request.forms.get('price')
        car.available = request.forms.get('available')
        # redirect the user to the car's info page
        redirect("/cars/%s/" % id)
    except Exception as e:
        print(str(e))
        redirect('/cars/%s/edit' % id)

'''
    The method provide form to add car to database
'''
@route('/cars/add')
def add_car():
    #get current list of brands to choose from
    brands = Brand.select()
    # render the form using the add_car template and send possible brands to form
    return template('cars/add', brands=brands)

'''
Takes info from add car form and creates new car in db
'''

@route('/cars/add', method='POST')
def new_car():
    try:
        brand = Brand.get(lambda b: b.name == request.forms.get('brand'))
        model = request.forms.get('model')
        price = int(request.forms.get('price'))
        available = int(request.forms.get('available'))
        Car(brand=brand,model=model,price=price,available=available)
        redirect('/cars')
    except Exception as e:
        redirect('/cars/add')
        print(str(e))
    
    
'''
Deletes car from db
'''
@route('/cars/<id>/delete', method='POST')
def delete_car(id):
    car = Car[id]
    car.delete()
    redirect('/cars')
    
'''
Search function that will return relevant search material, or an empty list if nothing is found
'''
@route('/cars/search', method='POST')
def car_with_brand():
    try:
        key = request.forms.get('key')
        cars = Car.select(lambda c: c.brand.name==str(key))
        if len(cars)!=0:
            return template('cars/search', cars=cars)
        cars = Car.select(lambda c: c.model==str(key))
        if len(cars)!= 0:
            return template('cars/search', cars=cars)
        cars = Car.select(lambda c: c.price <= int(key))
        if len(cars)!=0:
            return template('cars/search', cars=cars)
        cars = []
        return template('cars/search', cars=cars)
    except Exception:
        cars = []
        return template('cars/search', cars=cars)

#######################################
######## Customer functions ###########
#######################################
'''
lists all customers
'''
@route('/customers')
def all_customers():
    custs = select(c for c in Customer)
    return template('customers/index', custs=custs)

'''
Shows specific customer
'''
@route('/customers/<id>/')
def show_cust(id):
    cust = Customer[id]
    return template('customers/show', cust=cust)

'''
Displays form to add a customer to db
'''
@route('/customers/add')
def add_cust():
    return template('customers/add')


'''
Uses info from form for adding customer to add customer to db
'''
@route('/customers/add', method='POST')
def new_cust():
    try:
        name = request.forms.get('name')
        surname = request.forms.get('surname')
        phone = request.forms.get('phone')
        Customer(name=name,surname=surname,phone=phone)
        redirect('/customers')
    except Exception as e:
        print(str(e))
        redirect('/customers/add')

'''
    display form to edit customer
'''
@route('/customers/<id>/edit')
def edit_customer(id):
    # retrieve the student by id from the database
    cust = Customer[id]
    # render the form using the edit template for students
    return template('customers/edit', cust = cust)

'''
   Take input from form and update customers
'''
@route('/customers/<id>/edit', method='POST')
def update_cust(id):
    try:
        # retrieve the car by id from the database
        cust = Customer[id]
        # updating the brand, model, price and availability
        cust.name = request.forms.get('name')
        cust.surname=request.forms.get('surname')
        cust.phone=request.forms.get('phone')
        # redirect the user to the car's info page
        redirect("/customers/%s/" % id)
    except Exception as e:
        print(str(e))
        redirect('/customers/%s/edit' % id)

'''
Delete method for customer
'''
@route('/customers/<id>/delete', method="POST")
def delete_cust(id):
    cust = Customer[id]
    cust.delete()
    redirect('/customers')
    
'''
search for customers by name or surname, return empty list if nothing found
'''
@route('/customers/search', method='POST')
def search_cust():
    try:
        key = request.forms.get('key')
        print("got key")
        custs = Customer.select(lambda c: c.name == str(key))
        if len(custs)!=0:
            print(len(custs))
            return template('customers/search', custs=custs)
        custs = Customer.select(lambda c: c.surname == str(key))
        if len(custs)!= 0:
            print("found surname")
            return template('customers/search', custs=custs)
        custs = []
        return template('customers/search', custs=custs)
    except Exception:
        custs = []
        return template('customers/search', custs=custs)


#######################################
########### Order functions ###########
#######################################
'''
List all orders
'''
@route('/orders')
def all_orders():
    orders = select(o for o in Order)
    return template('orders/index', orders=orders)

'''
Show specific order info
'''
@route('/orders/<id>/')
def show_order(id):
    order = Order[id]
    curr_car_ids = []
    for c in order.cars.select()[:]:
        curr_car_ids.append(c.car_id)
    return template('orders/show', order=order)
'''
display form to add order to db
'''
@route('/orders/add')
def add_order():
    custs = Customer.select()
    cars = Car.select(lambda c: c.available != 0)
    return template('orders/add', custs=custs, cars=cars)

'''
retrieve info from add order form and add new order to db
'''
@route('/orders/add', method='POST')
def new_order():
    try:
        #id is located at beginning of string dispalyed to screen,
        #so split string around spaces and get the id from index 0
        id = request.forms.get('cust').split(' ')[0]
        cust = Customer.get(lambda c: c.cust_id==id)
        date = str(datetime.datetime.now())
        order = Order(cust=cust, total = -1, pdate = date)
        #holds car_id of each of selected car
        total = 0
        cars = request.forms.getall('car')
        #c = car_id of each checked car
        for c in cars:
            car = Car.get(lambda i: i.car_id == c)
            order.cars.add(car)
            total += car.price
            car.available -= 1
        order.total = total
        redirect('/orders')
    except Exception as e:
        print(str(e))
        redirect('/orders/add')


'''
Add new customer from the new order screen
'''
@route('/orders/customers/add')
def add_cust_order():
    return template('orders/customers/add')

'''
Handle form info from new customer for an order form and redirect to the new order page
'''
@route('/orders/customers/add', method="POST")
def new_cust_order():
    try:
        name = request.forms.get('name')
        surname = request.forms.get('surname')
        phone = request.forms.get('phone')
        Customer(name=name,surname=surname,phone=phone)
        redirect('/orders/add')
    except Exception as e:
        print(str(e))
        redirect('/orders/customers/add')

'''
    Display form to edit order contents. Can only edit the customer who ordered, and what they ordered.
'''
@route('/orders/<id>/edit')
def edit_order(id):
    # retrieve the student by id from the database
    order = Order[id]
    custs = Customer.select()
    cars = Car.select()
    #create list of current cars in the order to return
    #curr_cars = order.cars.select()[:]
    curr_car_ids = []
    for c in order.cars.select()[:]:
        curr_car_ids.append(c.car_id)
    # render the form using the edit template for students
    return template('orders/edit', order=order, custs = custs, cars=cars, curr_car_ids=curr_car_ids)


'''
    Take info from edit order form and edit existing order entry in db
'''
@route('/orders/<id>/edit', method='POST')
def update_order(id):
    try:
        #id is located at beginning of string dispalyed to screen,
        #so split string around spaces and get the id from index 0
        order = Order[id]
        cust_id = request.forms.get('cust').split(' ')[0]
        cust = Customer.get(lambda c: c.cust_id==cust_id)
        order.cust = cust
        date = str(datetime.datetime.now())
        order.pdate = date
        total = 0
        for car in order.cars:
            #assume cars may have been returned and increase availability
            car.available +=1
        order.cars.clear()
        cars = request.forms.getall('car')
        #c = car_id of each checked car
        for c in cars:
            car = Car.get(lambda i: i.car_id == c)
            order.cars.add(car)
            total += car.price
            #decrement availability by 1
            car.available -= 1
        order.total = total
        redirect('/orders/%s/' %id)
    except Exception as e:
        print(str(e))
        redirect('/orders/%s/edit' % id)
    
'''
deletes existing order entry in db
'''
@route('/orders/<id>/delete', method='POST')
def delete_order(id):
    order = Order[id]
    order.delete()
    redirect('/orders')

'''
searches for order by customer name, last name, or order number, returns empty list otherwise
'''
@route('/orders/search', method='POST')
def search_orders():
    try:
        key = request.forms.get('key')
        orders = Order.select(lambda o: o.cust.name == str(key))
        if len(orders)!=0:
            return template('orders/search', orders=orders)
        orders = Order.select(lambda o: o.cust.surname == str(key))
        if len(orders)!= 0:
            return template('orders/search', orders=orders)
        orders = Order.select(lambda o: o.order_num==int(key))
        return template('orders/search', orders=orders)
    except Exception:
        orders = []
        return template('orders/search', cars=cars)



                    
run(host='localhost', port=8080, debug=True)
