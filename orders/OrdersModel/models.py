from django.db import models

# Create your models here.
## 订单表
class Orders(models.Model):
    order_id = models.BigIntegerField(primary_key=True, unique=True)
    parent_order_id = models.BigIntegerField(db_index=True)  
class Orders_Time(models.Model):
    father_id = models.CharField(max_length=20)