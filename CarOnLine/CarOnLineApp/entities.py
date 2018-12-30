from pony.orm import *
import config
import json

db = Database()
'''
Brand: name, nationality
'''
class Brand(db.Entity):
    brand_id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    nation = Required(str)
    cars = Set('Car')


'''
Car: Brand, model, price, availibility
'''
class Car(db.Entity):
    car_id = PrimaryKey(int, auto=True)
    brand = Required('Brand')
    model = Required(str)
    price = Required(int)
    available = Required(int)
    orders = Set('Order')




'''
Customer: name, surname, phone number
'''
class Customer(db.Entity):
    cust_id = PrimaryKey(int, auto=True)
    name = Required(str)
    surname = Required(str)
    phone = Required(str)
    orders = Set('Order')


'''
Order: customer info, date of purchase, list of cars bought by customer
'''
class Order(db.Entity):
    order_num = PrimaryKey(int, auto=True)
    cust = Required('Customer')
    cars = Set('Car')
    total = Required(int)
    pdate = Required(str)


#######################################################
### The following 2 instructions bind the db to the
### SQLite file and generate the tables if needed.
#######################################################
# binding the entities to an sqlite database
db.bind('sqlite', config.DB_TEST, create_db=True)

# create the tables
db.generate_mapping(create_tables=True)
