import hashlib
import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# 首页
from hangowang.models import Lunbotu, User


def index(request):
    token = request.COOKIES.get('token')
    print(521)
    print(token)
    users = User.objects.filter(token=token)
    print(users)
    if users.exists():
        user = users.first()
        return render(request,'html/index.html',context={'user':user,'token':token})
    else:
        return render(request,'html/index.html')
# 登陆页面
def login(request):
    if request.method == 'GET':
        return render(request,'html/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        users = User.objects.filter(username=username,password=password)
        if users.exists():
            user = users.first()
            user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))
            user.save()
            response = redirect('hangowang:index')
            response.set_cookie('token',user.token)
            return response
        else:
            return HttpResponse('您的账号或密码有误，请查验后登录！')
# 注册页面
def register(request):
    if request.method == 'GET':
        return render(request,'html/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        addr = request.POST.get('addr')

        # 实例化用户对象
        user = User()
        user.username = username
        user.password = password
        user.addr = addr
        # token
        user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))
        # 保存用户
        user.save()
        # 重定向回首页
        response = redirect('hangowang:index')
        # 状态保持
        response.set_cookie('token',user.token)

        return response
# 密码
def generate_password(password):
    sha = hashlib.sha512()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()
# 退出登录
def logout(request):
    response = redirect('hangowang:index')
    response.delete_cookie('token')
    return response
# 商品详情页
def details(request):
    return render(request,'html/details.html')

# 购物车
def cart(request):
    return render(request,'html/cart.html')