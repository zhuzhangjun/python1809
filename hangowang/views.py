import hashlib
import uuid

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# 首页
from hangowang.models import Lunbotu, User


def index(request):
    token = request.session.get('token')
    if token:
        user = User.objects.get(token=token)
        username = user.username
    else:
        pass
    data = {
        'username': 'username'
    }
    return render(request,'html/index.html',context=data)
# 登陆页面
def login(request):
    return render(request,'html/login.html')

# 注册页面
def register(request):
    if request.method == 'GET':
        return render(request,'html/register.html')
    elif request.method == 'POST':
        user = User()
        user.username = request.POST.get('username')
        user.password = generate_password(request.POST.get('password'))
        user.addr = request.POST.get('addr')
        # token
        user.token = str(uuid.uuid5(uuid.uuid4(), 'register'))
        # 用户保存
        user.save()
        # 状态保持
        request.session['token'] = user.token
        # 重定向
        return redirect('hangowang:index')

# 密码
def generate_password(password):
    sha = hashlib.sha512()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()

# 退出登录
def logout(request):
    logout(request)
    return redirect('hangowang:index')

def details(request):
    return render(request,'html/details.html')


def cart(request):
    return render(request,'html/cart.html')