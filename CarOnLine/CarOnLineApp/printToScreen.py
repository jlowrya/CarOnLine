from pony.orm import *
import json
import config
from entities import *

@db_session
def print_brands():
    for brand in Brand.select():
        print(brand.name+" "+brand.nation)
        for c in brand.cars:
            print(c.model+" "+str(c.price)+" "+str(c.available))

if __name__ == "__main__":
    print_brands()
