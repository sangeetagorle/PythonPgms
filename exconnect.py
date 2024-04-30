import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='Bruno80@8088',database='kod')
c=con.cursor()
c.execute("delete from emp where name='raj'")
con.commit()
c.execute("select * from emp")
print(c.fetchall())

    

