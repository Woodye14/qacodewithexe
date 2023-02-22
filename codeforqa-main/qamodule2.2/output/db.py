import _sqlite3 as sql 
conn = sql.connect("workers.db")
cursor = conn.cursor()


#def CreatingTable():
#      sql_file = open("employees.sql")
 #     sql_string = sql_file.read()
#      cursor.executescript(sql_string)

def selectQuery(query):
    return cursor.execute(query).fetchall()

def dataQuery(query):
    cursor.execute(query)
    return True

def commitChanges():
    conn.commit()

#CreatingTable()