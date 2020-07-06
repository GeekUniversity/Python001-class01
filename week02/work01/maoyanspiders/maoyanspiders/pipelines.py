# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd
import  pymysql


class MaoyanspidersPipeline:
    def __init__(self):
        self.conn = pymysql.connect(
            host='192.168.204.100',
            port=3306,
            user='repl',
            passwd='3edc$RFV',
            db='movies',
            charset='utf8'
        )
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into movies(movie_name,movie_time,movie_type) VALUES (%s,%s,%s)'
        list = (item['movie_name'], item['movie_time'], item['movie_type'])
        self.cur.execute(sql, list)
        self.conn.commit()

    def __del__(self):
        self.conn.close()

