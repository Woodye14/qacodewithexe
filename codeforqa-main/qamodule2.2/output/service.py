from db import *

def insertEmployee():
    employee_name = input("please enter employee name ")
    team = input("insert team name: ")
    employed = input("employed? (true/false): ")
    employee_query = f"INSERT INTO employees (employee_name, team_name, employee_working) VALUES ('{employee_name}', '{team}', '{employed}');"
    cursor.execute(employee_query)
    return True

def readName(query):
    return cursor.execute(query).fetchall()

def readAllEmployees():
    query = "SELECT * FROM employees"
    return readName(query)

def deleteName():
    id = input("what is the ID of the name you would like to delete?")
    query = f"DELETE FROM employees where employee_id = {id}"
    return dataQuery(query)

def updateName():
    id = input("what is the name you would like to update:")
    name = input("what would you like the new name to be")
    query = f"UPDATE employees SET employee_name = '{name}' WHERE employee_id = {id}"
    return dataQuery(query)


conn.commit()