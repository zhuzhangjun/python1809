import hashlib
import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# 首页
from hangowang.models import Lunbotu, User, Daydown, Gitpush, Goodlists, DaydownDetail


def index(request):
    token = request.COOKIES.get('token')
    users = User.objects.filter(token=token)
    lunbotu_list = Lunbotu.objects.all()
    w390 = Daydown.objects.all()[0:2]
    w480 = Daydown.objects.all()[2:6]
    w320 = Daydown.objects.all()[6:8]
    gitpush = Gitpush.objects.all()
    right_side = Goodlists.objects.first()
    productList4_head = Goodlists.objects.all()[1:3]
    center_side = Goodlists.objects.all()[3:4]
    productList4_foot = Goodlists.objects.all()[4:10]
    data = {
        'lunbotu_list': lunbotu_list,
        'w390': w390, 'w480': w480,
        'w320': w320,
        'gitpush': gitpush,
        'right_side': right_side,
        'productList4_head': productList4_head,
        'center_side': center_side,
        'productList4_foot': productList4_foot,
    }
    if users.exists():
        user = users.first()
        data['user'] = user
        data['token'] = token
        return render(request,'html/index.html',context=data)
    else:
        return render(request,'html/index.html',context=data)
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
def details(request,detail):
    daydown = Daydown.objects.get(pk=detail)
    detail_info = daydown.daydowndetail

    return render(request,'html/details.html',context={'detail_info':detail_info})

# 购物车
def cart(request):
    return render(request,'html/cart.html')