#!/usr/bin/python3

"""
Class for the Database Storage
"""
import os

class DBStorage():
    """Database"""
    __engine = None
    __session = None

    # SETTING ENVIRONMENT VARIABLES
    ENV = os.environ
    user = ENV["HBNB_MYSQL_USER"] = "hbnb_dev"
    dbb = ENV["HBNB_MYSQL_DB"] = "hbnb_dev_db"
    pwd = ENV["HBNB_MYSQL_PWD"] = "hbnb_dev_pwd"
    host = ENV["HBNB_MYSQL_HOST"] = "localhost"

    def __init__(self):
        """Creates engine that links to database"""
        db_engine = 'mysql+mysqldb://{}:{}@{}/{}'.format(
                user, pwd, host, dbb)
        self.__engine = create_engine(db_engine, pool_pre_ping=True)

    def all(self, cls=None):

