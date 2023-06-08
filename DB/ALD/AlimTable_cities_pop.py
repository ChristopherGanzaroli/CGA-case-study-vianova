from Class.DBConnection import sqlitConn
import sqlite3
from sqlite3 import Error
import csv
import sys
sys.path.append("../../")

###################################################################################################
##                                      OPEN DATA                                                ##
###################################################################################################

with open('/Users/ganza/OneDrive/Bureau/gitripo/tests/vianova/Data/cities_pop_from_csv.csv', 'r', encoding="utf-8-sig") as data:
    dr = csv.DictReader(data, delimiter=';')

    # FROM API (do not forget to remove the delimiter ";" in dr = csv.DictReader(data,delimiter=';'))
    # to_db_from_api = [(i['geoname_id'], i['name'],i['ascii_name'],i['alternate_names'],i['feature_class'],i['feature_code'],i['country_code'],i['cou_name_en'],i['admin1_code'],i['admin2_code'],i['admin3_code'],i['admin4_code'],i['population'],i['elevation'],i['dem'],i['timezone'],i['modification_date'],i['label_en'],i['Coordinates']) for i in dr]

    # FROM CSV
    to_db_from_csv = [(i['Geoname ID'], i['Name'], i['ASCII Name'], i['Alternate Names'], i['Feature Class'], i['Feature Code'], i['Country Code'], i['Country name EN'], i['Admin1 Code'], i['Admin2 Code'],
                       i['Admin3 Code'], i['Admin4 Code'], i['Population'], i['Elevation'], i['DIgital Elevation Model'], i['Timezone'], i['Modification date'], i['LABEL EN'], i['Coordinates']) for i in dr]

    ###################################################################################################
    ##                                      DATA FEEDING                                             ##
    ###################################################################################################


def ald_cities_pop():
    try:

        conn = sqlite3.connect(
            "/Users/ganza/OneDrive/Bureau/gitripo/tests/vianova/DB/db.sqlite")
        cur = conn.cursor()
        cur.execute("DELETE FROM cities_pop;")
        cur.executemany("INSERT INTO cities_pop (geoname_id,name,ascii_name,alternate_names,'feature_class',feature_code,country_code,cou_name_en,admin1_code,admin2_code,admin3_code,admin4_code,population,elevation,dem,timezone,modification_date,label_en,Coordinates) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", to_db_from_csv)
        conn.commit()
        conn.close()

    except Error as e:
        print(e)


ald_cities_pop()
