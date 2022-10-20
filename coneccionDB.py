import pymysql
db = pymysql.connect (
    user = "",
    password = "",
    host = "",
    port = ,
    database = ""
)
Cursor = db.cursor()
resultado = Cursor.execute( "")
resultado = Cursor.fetchone()
print(resultado)