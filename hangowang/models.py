from django.db import models

# Create your models here.

# 轮播图　模型类
class Lunbotu(models.Model):
    id = models.IntegerField(primary_key=True)
    src = models.CharField(max_length=30)
    class Meta:
        db_table = 'Lunbotu'
# 用户模型类
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    addr = models.CharField(max_length=50)
    token = models.CharField(max_length=100)
    class Meta:
        db_table = 'User'
# 今日优惠模型类
class Daydown(models.Model):
    imgsrc = models.CharField(max_length=20)
    class Meta:
        db_table = 'daydown'
# 推荐模型类
class Gitpush(models.Model):
    imgsrc = models.CharField(max_length=30)
    class Meta:
        db_table = 'gitpush'
# 粮油杂货模型类
class Goodlists(models.Model):
    img = models.CharField(max_length=30)
    goodsname = models.CharField(max_length=100)
    price = models.FloatField()
    oldprice = models.FloatField()
    class Meta:
        db_table = 'Goodlists'
