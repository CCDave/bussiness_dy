from django.db import models

# Create your models here.
# Create your models here.
class Orders(models.Model):
    father_id = models.CharField(max_length=20)


class Orders_Time(models.Model):
    father_id = models.CharField(max_length=20)