from django.db import models

# Create your models here.

class ProductInfo(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_describe = models.TextField(blank=True, null=True)
    spider_time = models.DateTimeField()
    product_name = models.CharField(max_length=500, blank=True, null=True)
    worthy_num = models.IntegerField(blank=True, null=True)
    unworthy_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_info'



class Assessment(models.Model):
    assess_id = models.AutoField(primary_key=True)
    product = models.ForeignKey('ProductInfo', models.DO_NOTHING)
    assess_content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment'
