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

    # Executing the SQL query to select states starting with 'N'
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")

    # Fetching all the rows resulted from the query and printing each row
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Closing the cursor and database connection
    cur.close()
    db.close()
