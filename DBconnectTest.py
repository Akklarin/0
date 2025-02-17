import psycopg2 as pg


try:
    conn = pg.connect(
        host='localhost',
        database='BHhw',
        port=5432,
        user='postgres',
        password='{__MyPASSWORD__}'
    )

    cursor = conn.cursor()
    print("Connection established.")

except Exception as err:
    print("Something went wrong.")
    print(err)


