import mysql.connector

udemy = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="udemy"
)

column_cursor = udemy.cursor()
column_cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'priyaprem08';")
coulmns_priyaprem08 = column_cursor.fetchall()

column_cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'priyadharshini170898';")
columns_priyadharshini170898 = column_cursor.fetchall()

column_cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'priyadharshini221099';")
columns_priyadharshini221099 = column_cursor.fetchall()

columns = {
    'priyaprem08': [],
    'priyadharshini170898': [],
    'priyadharshini221099': []
}


for x in coulmns_priyaprem08:
    columns['priyaprem08'].extend(x)

for x in columns_priyadharshini170898:
    columns['priyadharshini170898'].extend(x)

for x in columns_priyadharshini221099:
    columns['priyadharshini221099'].extend(x)

print(len(columns['priyaprem08']))


print(len(columns['priyadharshini170898']))


print(len(columns['priyadharshini221099']))

