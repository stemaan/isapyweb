import sqlite3
from pprint import pprint

with sqlite3.connect('test.db') as conn:
    query = 'SELECT * FROM films;'
    cursor = conn.execute(query)
    result = cursor.fetchall()
    pprint(result)
