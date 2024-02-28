import sqlite3

def connect():
    connection=sqlite3.connect("crime.db")
    cur=connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS crime_record( Criminal_id PRIMARY KEY,Name text,Gender text,Nationality text,Age integer,Height float,Weight float,Crime_Committed text)")
    connection.commit()
    # connection.close()

def insert(Criminal_id,Name,Gender,Nationality,Age,Height,Weight,Crime_Committed):
    connection=sqlite3.connect("crime.db")
    cur=connection.cursor()
    cur.execute("INSERT INTO crime_record VALUES (?, ?, ?, ?, ?, ?, ?, ?)",(Criminal_id , Name , Gender , Nationality , Age , Height , Weight , Crime_Committed))
    connection.commit()
    # connection.close()

def view():
    connection=sqlite3.connect("crime.db")
    cur=connection.cursor()
    cur.execute("SELECT * FROM crime_record ")
    rows=cur.fetchall()
    # connection.close()
    return rows

def search(Criminal_id="",Name="",Gender="",Nationality="",Age="",Height="",Weight="",Crime_Committed=""):
    connection=sqlite3.connect("crime.db")
    cur=connection.cursor()
    cur.execute("SELECT * FROM crime_record WHERE Criminal_id=? OR Name=? OR Gender=? OR Nationality=? OR Age=? OR Height=? OR Weight=? OR Crime_Committed=? ",(Criminal_id,Name,Gender,Nationality,Age,Height,Weight,Crime_Committed))
    rows=cur.fetchall()
    # connection.close()
    return rows

def delete(Criminal_id):
    connection=sqlite3.connect("crime.db")
    cur=connection.cursor()
    cur.execute("DELETE FROM crime_record WHERE Criminal_id=?",(Criminal_id,))
    connection.commit()
    # connection.close()

def update(Criminal_id,Name,Gender,Nationality,Age,Height,Weight,Crime_Committed):
    connection=sqlite3.connect("crime.db")
    cur=connection.cursor()
    cur.execute("UPDATE crime_record SET Criminal_id=?,Name=?,Gender=?,Nationality=?,Age=?,Height=?,Weight=?,Crime_Committed=?  WHERE Criminal_id=?",(Criminal_id,Name,Gender,Nationality,Age,Height,Weight,Crime_Committed,Criminal_id))
    connection.commit()
    # connection.close()

connect()

