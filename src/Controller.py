from mysql.connector import *

host = 'localhost'
user = 'matt'
password = 'password'

# Write Function to list all citys in salkila database

def get_all_cities():
    # Step 1: Create Connection Object
    with connect(host=host, user=user, password=password) as mysql_connection_object:
        # Step 2: Create a cursor object
        with mysql_connection_object.cursor() as mysql_cursor:
            # Step 3: Create a Query and execute
            display_city = f"select * from sakila.city;"
            mysql_cursor.execute(display_city)
            #Step 4: Fetch all data returned after query execution
            all_cities = mysql_cursor.fetchall()
            print(all_cities)

get_all_cities()