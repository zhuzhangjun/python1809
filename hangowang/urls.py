from django.conf.urls import url

from hangowang import views

urlpatterns = [
    url(r'^$',views.index,name='index'),  # 首页
    url(r'^index/$',views.index,name='index'),  # 首页
    url(r'^login/$',views.login,name='login'),  # 登录
    url(r'^register/$',views.register,name='register'),  # 注册
    url(r'^details/$',views.details,name='details'),  # 商品详情页面
    url(r'^cart/$',views.cart,name='cart'),  # 购物车页面
]