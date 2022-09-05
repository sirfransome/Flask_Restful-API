import psycopg2

connection = psycopg2.connect(host='server_name.amazonaws.com',
                              user='user',
                              password='password',
                              database='database',
                              port=1234,)

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users_table (userid INTEGER , username varchar(256), password varchar(256), primary key(userid))"
cursor.execute(create_table)

connection.commit()
connection.close()