import MySQLdb

def connection():
    conn = MySQLdb.connect(host="sql9.freemysqlhosting.net",
                           user="sql9167459",
                           passwd="HVrici4rxI",
                           db = "sql9167459")
    c = conn.cursor()

    return c, conn
