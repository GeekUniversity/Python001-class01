# Author Andy Fang
# -*- coding:utf-8 -*-

import  pymysql

def insert_production(prodution_name, production_describe,worthy_num, unworthy_num):
    conn = pymysql.connect(
        host='192.168.204.100',
        port=3306,
        user='repl',
        passwd='3edc$RFV',
        db='db02',
        charset='utf8mb4'
    )
    cur = conn.cursor()
    sql = 'insert into product_info(product_name,product_describe,worthy_num,unworthy_num) VALUES (%s,%s,%s,%s)'
    li = [prodution_name, production_describe,worthy_num, unworthy_num]
    cur.execute(sql, li)
    conn.commit()
    id = cur.lastrowid
    conn.close()
    return  id