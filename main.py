from Class.DBConnection import sqlitConn
import csv
from sqlite3 import Error
import sys
sys.path.append("..")


def main():
    
    ###################################################################################################
    ##                                      SQL QUERY                                                ##
    ###################################################################################################

    def readSqliteTable():
        try:
            sqliteConnection = sqlitConn('db.sqlite').create_connection()

            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sqlite_select_query = """
                                    SELECT geoname_id, name,country_code, population
                                    FROM cities_pop
                                    GROUP BY country_code
                                    HAVING MAX(population) < 10000000
                                """
            cursor.execute(sqlite_select_query)
            records = cursor.fetchall()

            cursor.close()

            return records

        except Error as error:
            print("Failed to read data from sqlite table", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
                
    ###################################################################################################
    ##                                      DATA EXPORT                                              ##
    ###################################################################################################

    with open('response.csv', 'w', newline='', encoding='utf-8') as file:
        # Ecrire dans le ficher avec les noms de colonnes
        writer = csv.writer(file, delimiter=',')
        # on crée les colonnes du fichier
        writer.writerow(['geoname_id', 'cou_name_en',
                        'ascii_name', 'country_code'])
        data = readSqliteTable()
        for i in range(len(data)):
            geoname_id = data[i][0]
            cou_name_en = data[i][1]
            ascii_name = data[i][2]
            country_code = data[i][3]

            writer.writerow(
                [geoname_id, cou_name_en, ascii_name, country_code])
    #print(readSqliteTable())


main()
