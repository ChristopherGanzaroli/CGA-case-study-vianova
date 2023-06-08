import sqlite3
from sqlite3 import Error
import os

class sqlitConn :
    """
    this class creates a connection to the database by retrieving its path 
    
    result : path/DB/ + self.db_name
    """
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    global db_path
    db_path = os.getcwd()+'/'
    db_path = db_path.replace('\\','/')[2:-1]+"/DB/"
    
    def __init__(self, db_file) :
 
        self.db_file = db_file
        
    
    def create_connection(self):

        conn = None
        try:
            print(db_path+self.db_file)
            conn = sqlite3.connect(db_path+self.db_file)
            
        except Error as e:
            print(e)

        return conn

