import sqlite3
from pprint import pprint

with sqlite3.connect('test.db') as conn:
    conn.row_factory = sqlite3.Row
    query = 'SELECT * FROM films;'
    cursor = conn.execute(query)
    result = [dict(row) for row in cursor.fetchall()]
    pprint(result)
