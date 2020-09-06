# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class SpidersPipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host='192.168.204.100',
            port=3306,
            user='repl',
            passwd='3edc$RFV',
            db='db02',
            charset='utf8mb4'
        )
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        list = (item['product_id'], item['assess_content'])
        check_sql = 'select * from assessment where  product_id=%s and assess_content=%s'
        result = self.cur.execute(check_sql, list)
        #去重
        if result == 0:
            sql = 'insert into assessment(product_id,assess_content) VALUES (%s,%s)'
            self.cur.execute(sql, list)
            self.conn.commit()

    def __del__(self):
        self.conn.close()
