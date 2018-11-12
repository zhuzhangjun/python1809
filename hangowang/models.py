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
    id = models.CharField(max_length=10,primary_key=True)
    imgsrc = models.CharField(max_length=20)
    isselect = models.BooleanField(default=False)
    class Meta:
        db_table = 'daydown'
# 推荐模型类
class Gitpush(models.Model):
    imgsrc = models.CharField(max_length=30)
    class Meta:
        db_table = 'gitpush'
# 粮油杂货模型类
class Goodlists(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    img = models.CharField(max_length=30)
    goodsname = models.CharField(max_length=100)
    price = models.FloatField()
    oldprice = models.FloatField()
    isselect = models.BooleanField(default=False)
    class Meta:
        db_table = 'Goodlists'
# 今日优惠_详情信息
class DaydownDetail(models.Model):
    shopname = models.CharField(max_length=50,null=True)
    imgsrc = models.CharField(max_length=50)
    middleimg1 = models.CharField(max_length=50,null=True)
    middleimg2 = models.CharField(max_length=50,null=True)
    middleimg3 = models.CharField(max_length=50,null=True)
    middleimg4 = models.CharField(max_length=50,null=True)
    smallimg1 = models.CharField(max_length=50,null=True)
    smallimg2 = models.CharField(max_length=50,null=True)
    smallimg3 = models.CharField(max_length=50,null=True)
    smallimg4 = models.CharField(max_length=50,null=True)
    bigimg1 = models.CharField(max_length=50,null=True)
    bigimg2 = models.CharField(max_length=50,null=True)
    bigimg3 = models.CharField(max_length=50,null=True)
    bigimg4 = models.CharField(max_length=50,null=True)
    dtbgimg1 = models.CharField(max_length=50,null=True)
    dtbgimg2 = models.CharField(max_length=50,null=True)
    dtbgimg3 = models.CharField(max_length=50,null=True)
    dtbgimg4 = models.CharField(max_length=50,null=True)
    dtbgimg5 = models.CharField(max_length=50,null=True)
    dtbgimg6 = models.CharField(max_length=50,null=True)
    dtbgimg7 = models.CharField(max_length=50,null=True)
    dtbgimg8 = models.CharField(max_length=50,null=True)
    hint = models.CharField(max_length=50,null=True) # 【特价商品不接券】
    evaluate = models.CharField(max_length=10,null=True)
    repertory = models.CharField(max_length=10,null=True)
    title = models.CharField(max_length=100,null=True) # 特产稻香长粒大米10斤 非转基因长粒大米 香糯清甜【荆门农谷鲜】
    unit = models.CharField(max_length=10,null=True)
    price = models.CharField(max_length=10,null=True)
    original = models.CharField(max_length=10,null=True)

    daydown = models.OneToOneField(Daydown)
    class Meta:
        db_table = 'daydown_Detail'

#粮油杂货_详情信息
class GoodsDetail(models.Model):
    shopname = models.CharField(max_length=50,null=True)
    imgsrc = models.CharField(max_length=50)
    middleimg1 = models.CharField(max_length=50,null=True)
    middleimg2 = models.CharField(max_length=50,null=True)
    middleimg3 = models.CharField(max_length=50,null=True)
    middleimg4 = models.CharField(max_length=50,null=True)
    smallimg1 = models.CharField(max_length=50,null=True)
    smallimg2 = models.CharField(max_length=50,null=True)
    smallimg3 = models.CharField(max_length=50,null=True)
    smallimg4 = models.CharField(max_length=50,null=True)
    bigimg1 = models.CharField(max_length=50,null=True)
    bigimg2 = models.CharField(max_length=50,null=True)
    bigimg3 = models.CharField(max_length=50,null=True)
    bigimg4 = models.CharField(max_length=50,null=True)
    dtbgimg1 = models.CharField(max_length=50,null=True)
    dtbgimg2 = models.CharField(max_length=50,null=True)
    dtbgimg3 = models.CharField(max_length=50,null=True)
    dtbgimg4 = models.CharField(max_length=50,null=True)
    dtbgimg5 = models.CharField(max_length=50,null=True)
    dtbgimg6 = models.CharField(max_length=50,null=True)
    dtbgimg7 = models.CharField(max_length=50,null=True)
    dtbgimg8 = models.CharField(max_length=50,null=True)
    hint = models.CharField(max_length=50,null=True) # 【特价商品不接券】
    evaluate = models.CharField(max_length=10,null=True)
    repertory = models.CharField(max_length=10,null=True)
    title = models.CharField(max_length=100,null=True) # 特产稻香长粒大米10斤 非转基因长粒大米 香糯清甜【荆门农谷鲜】
    unit = models.CharField(max_length=10,null=True)
    price = models.CharField(max_length=10,null=True)
    original = models.CharField(max_length=10,null=True)

    Goods = models.OneToOneField(Goodlists)
    class Meta:
        db_table = 'Goods_Detail'









