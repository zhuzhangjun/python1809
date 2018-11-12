from django.conf.urls import url

from hangowang import views

urlpatterns = [
    url(r'^$',views.index,name='index'),  # 首页
    url(r'^login/$',views.login,name='login'),  # 登录
    url(r'^register/$',views.register,name='register'),  # 注册
    url(r'^details/(\d+)/$',views.details,name='details'),  # 商品详情页面
    url(r'^details_goods/(\d+)/$',views.details_goods,name='details_goods'),  # 商品详情页面
    url(r'^cart/$',views.cart,name='cart'),  # 购物车页面
    url(r'^logout/$',views.logout,name='logout'),  # 退出登录

    url(r'addcart/(\d+)/$',views.addcart,name='添加购物车') # 添加购物车
]