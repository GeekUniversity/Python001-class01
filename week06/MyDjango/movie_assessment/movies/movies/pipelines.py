# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import  pymysql

class MoviesPipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host='192.168.204.100',
            port=3306,
            user='repl',
            passwd='3edc$RFV',
            db='db1',
            charset='utf8mb4'
        )
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into t1(n_star,short) VALUES (%s,%s)'
        list = (item['n_star'], item['short'])
        self.cur.execute(sql, list)
        self.conn.commit()

    def __del__(self):
        self.conn.close()
