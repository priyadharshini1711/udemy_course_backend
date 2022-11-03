import mysql.connector

udemy = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="udemy"
)

course_cursor = udemy.cursor()

course_cursor.execute("select id, content_info from priyaprem08;")
coulmns_priyaprem08 = course_cursor.fetchall()

course_cursor.execute("select id, content_info from priyadharshini170898;")
columns_priyadharshini170898 = course_cursor.fetchall()

course_cursor.execute("select id, content_info from priyadharshini221099;")
columns_priyadharshini221099 = course_cursor.fetchall()

course_time = {}


for x in coulmns_priyaprem08:
    time = x[1].split(" ")
    units = ""
    if(time[1].strip() == 'total'):
        units = time[2]
    else:
        units = time[1]
    course_time[x[0]] = [x[1], time[0], units, 1]

for x in columns_priyadharshini170898:
    if x[0] not in course_time:
        time = x[1].split(" ")
        units = ""
        if(time[1].strip() == 'total'):
            units = time[2]
        else:
            units = time[1]
        course_time[x[0]] = [x[1], time[0], units, 2]

for x in columns_priyadharshini221099:
    if x[0] not in course_time:
        time = x[1].split(" ")
        units = ""
        if(time[1].strip() == 'total'):
            units = time[2]
        else:
            units = time[1]
        course_time[x[0]] = [x[1], time[0], units, 3]

val = []

for k in course_time:
    temp = []
    temp.extend(course_time[k])
    temp.append(k)
    val.append(tuple(temp))

sql = 'insert into course_time (duration, time, units, user, id) values (%s,%s,%s,%s,%s)'

course_cursor.executemany(sql, val)

udemy.commit()