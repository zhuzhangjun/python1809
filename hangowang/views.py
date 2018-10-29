from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 首页
from hangowang.models import Lunbotu


def index(request):
    lunbotu_list = Lunbotu.objects.all()
    data = {
        'lunbotu_list': lunbotu_list
    }
    return render(request,'html/index.html',context=data)
# 登陆页面
def login(request):
    return render(request,'html/login.html')

# 注册页面
def register(request):
    return render(request,'html/register.html')


def details(request):
    return render(request,'html/details.html')


def cart(request):
    return render(request,'html/cart.html')