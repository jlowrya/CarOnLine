'''
    App configuration module
    ========================

    The config.py file contains all the configuration variable of your application.
    All the configuration parameters should be put here, since this file is
    imported by every module application.
    Since these are global variables, please use ALL CAPITAL notation.
'''

# DB_FILE_NAME : path to the SQLite database file.
DB_FILE_NAME = 'db/car_online.sqlite'

# DB_TEST :  path to test sql database that will be used for debugging during development
DB_TEST = 'db/test.sqlite'

# DB_DUMP_FILE_NAME : path to the json file that will be used to seed the database.
DB_DUMP_FILE_NAME = 'data/data.json'
