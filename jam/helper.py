import MySQLdb


class DB:
    def __init__(self):
        pass

    def connect(self):
        hostname = 'hostname'
        dbname = 'dbname'
        username = 'username'
        password = 'password'

        connection = MySQLdb.connect(hostname, username, password, dbname)
        return connection


    def getCursor(self):
        db = DB()
        con = db.connect()
        cursor = con.cursor()
        return con, cursor

    def closeCursor(self, con, cursor):
        con.commit()
        id_row = str(cursor.lastrowid)
        cursor.close()
        return id_row


    def queryInsert(self, table, columns, values):
        query = "INSERT INTO "+table+"("+columns+") VALUES("+values+")"
        print query
        try:
            con, cursor = self.getCursor()
            cursor.execute(query)
            id_row = self.closeCursor(con, cursor)
        except:
            id_row = "0"

        return id_row

    def querySelect(self, table, columns):
        query = "SELECT "+columns+" FROM "+table
        list_rows = []
        try:
            con, cursor = self.getCursor()
            cursor.execute(query)
            for row in cursor.fetchall():
                list_rows.append(row)
            id_row = self.closeCursor(con, cursor)
        except:
            id_row = "0"

        return id_row, list_rows

if __name__== "__main__":
    obj = DB()
    obj.querySelect("title", "name")
