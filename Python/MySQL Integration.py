# Python Integration with MySQL
import mysql.connector as m
c = m.connect(
    host = "local host" , user = "root" , password = "Password@" , database = "student")
p = c.cursor()
s = "select * from student;"
p.execute(s)
d = p.fetchall()
for i in d:
    print(i)
c.close()
