import sqlite3


def run_query(query, db):
    with sqlite3.connect(db) as conn:
        cursor = conn.execute(query)
        result = cursor.fetchall()
        return result


if __name__ == '__main__':
    from queries import QUERY_MAP
    import os

    dirname = os.path.dirname(__file__)
    db_name = 'clients.db'
    path_to_db = os.path.join(dirname, 'example_dbs', db_name)
    print(path_to_db)
    print(run_query(QUERY_MAP['all'], path_to_db))
