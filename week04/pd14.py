# Author Andy Fang
# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np
import pymysql

df = pd.read_excel('1.xlsx')
df1 = pd.read_excel('2.xlsx')

#SELECT * FROM data;
print(df)

#SELECT * FROM data LIMIT 10;
print(df.head(10))

#SELECT COUNT(id) FROM data;
print(df['id'])

#SELECT * FROM data WHERE id<1000 AND age>30;
print(df[(df['id']<1000)&(df['age']>30)])

#SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
print(df.groupby('id')['order_id'].nunique())

#SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
print(pd.merge(df,df1,on='id',how='inner'))

#SELECT * FROM table1 UNION SELECT * FROM table2;
print(pd.concat([df,df1]))


#DELETE FROM table1 WHERE id=10;
print(df[df['id']!=10])

#ALTER TABLE table1 DROP COLUMN column_name;
print(df.iloc[:,[0,2]])
# conn = pymysql.connect(host="192.168.204.100", user="repl", password="3edc$RFV", database='movies', charset="utf8")
# cursor = conn.cursor()
# sql = """
# create table table1(
#  id int,
#  order_id int,
#  age int
# )"""
# cursor.execute(sql)
# sql = 'insert into table1 values(%s,%s,%s);'
# for i in df.values.tolist():
#      cursor.execute(sql, i)
# conn.commit()
# conn.close()