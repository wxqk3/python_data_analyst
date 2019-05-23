from mysql import connector
conn=connector.connect(host='localhost',port='3306',user='root',password='',database='test',charset='utf8')

conn.autocommit=True

cursor=conn.cursor()

sqltext='select * from users'

cursor.execute(sqltext)

for row in cursor:
    print row