from django.db import models

# Create your models here.

# 轮播图　模型类
class Lunbotu(models.Model):
    id = models.IntegerField(primary_key=True)
    imgsrc = models.CharField(max_length=30)
    class Meta:
        db_table = 'Lunbotu'