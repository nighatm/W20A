import mariadb
import dbcreds

def insert_data():
    content = input("Add content: ")
    conn = mariadb.connect(user= dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database= dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO blog_post(username, content, id) VALUES(?, ?, NULL)", [username, content])

    conn.commit()

    cursor.close()
    conn.close()
    print("Record Entered")

def show_data():
    conn = mariadb.connect(user= dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database= dbcreds.database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM blog_post")
    rows=cursor.fetchall()
    print(rows)

    cursor.close()
    conn.close()