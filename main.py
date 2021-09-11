import cx_Oracle

try:
    connection = cx_Oracle.connect(
        user='PY',
        password='123456',
        dsn='localhost:1521/XE',
        encoding='UTF-8'
    )
    print(connection.version)

    c = connection.cursor()
    rows = c.execute("SELECT * FROM XPTO.COURSE_MATTERS").fetchall()

    print(rows)

except Exception as ex:
    print(ex)

