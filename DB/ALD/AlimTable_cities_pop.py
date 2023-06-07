import sqlite3
from sqlite3 import Error
import csv
import os.path

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# db_path = os.path.join(BASE_DIR, "db.sqlite")




with open('/Users/ganza/OneDrive/Bureau/gitripo/tests/vianova/Data/cities_pop.csv','r',encoding="utf8") as data: 
    dr = csv.DictReader(data) 
    to_db = [(i['geoname_id'], i['name'],i['ascii_name'],i['alternate_names'],i['feature_class'],i['feature_code'],i['country_code'],i['cou_name_en'],i['admin1_code'],i['admin2_code'],i['admin3_code'],i['admin4_code'],i['population'],i['elevation'],i['dem'],i['timezone'],i['modification_date'],i['label_en'],i['Coordinates']) for i in dr]


def ald_cities_pop() :
    try :
        conn = sqlite3.connect('/Users/ganza/OneDrive/Bureau/gitripo/tests/vianova/DB/db.sqlite')
        cur = conn.cursor()
        cur.executemany("INSERT INTO cities_pop (geoname_id,name,ascii_name,alternate_names,'feature_class',feature_code,country_code,cou_name_en,admin1_code,admin2_code,admin3_code,admin4_code,population,elevation,dem,timezone,modification_date,label_en,Coordinates) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);",to_db)
        conn.commit()
        conn.close()
        
    except Error as e:
        print(e)

ald_cities_pop()