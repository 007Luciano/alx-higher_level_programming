#!/usr/bin/python3
"""
Lists all states from the database
    Args:
        argv[1](string): Db username
        argv[2](string): Db password
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Establishing a connection to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    # Creating a cursor object to execute SQL queries
    cur = db.cursor()

    # Executing the SQL query to select cities belonging to a specific state
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))

    # Fetching all the rows resulted from the query
    rows = cur.fetchall()
    cities = [row[0] for row in rows]

    # Print the city names separated by commas
    print(*cities, sep=", ")

    # Closing the cursor and database connection
    cur.close()
    db.close()
