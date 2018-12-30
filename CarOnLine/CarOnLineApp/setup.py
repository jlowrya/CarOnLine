import json
import config
from entities import *
'''
    Setup module
    ===========

    The setup module should have all the methods that has to be executed before
    the application is started (i.e. seeding the database).
'''


'''
    Seed the database with information from the json dump file.
    NOTE:   this method is specific to each application, which means you have
            to write your import method for your application.
'''
@db_session
def seed_database(dump_filename):
    # reading the json file
    data = json.load(open(dump_filename, 'r'))

    # going through the list of brands
    for record in data['Brands']:
        # creating a new brand object for each entry
        brand = Brand(name = record['name'],
                          nation = record['nation'])

    # going through the list of cars
    for record in data['Cars']:
        car_brand = Brand.get(lambda b: b.name == record['brand'])
        # creating a new car object for each entry
        brand = Car(brand = car_brand, model=record['model'],price=record['price'],
                    available=record['available'])
    #going through the list of customers
    for record in data['Customers']:
        # creating a new customer object for each entry
        brand = Customer(name=record['name'], surname=record['surname'],
                         phone=record['phone'])

if __name__ == "__main__":
    seed_database(config.DB_DUMP_FILE_NAME)
