import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port=54320,
    dbname='mydb_psql',
    user='postgres',
    password='qwerty123',
)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS test2 (id serial PRIMARY KEY, num integer, data varchar);")
# cur.execute("INSERT INTO test2 (num, data) VALUES (%s, %s)", (100, "abcdef"))
# cur.execute("SELECT * FROM test;")
# result = cur.fetchone()
# print(result)
conn.commit()
cur.close()
conn.close()
