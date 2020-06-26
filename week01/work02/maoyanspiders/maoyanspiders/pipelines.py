# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas as pd

class MaoyanspidersPipeline:
    def process_item(self, item, spider):
        writer = pd.DataFrame([item])
        writer.to_csv('./top10_movies_info.csv',mode='a', encoding='utf_8_sig', index=False, header=False)
        return item
