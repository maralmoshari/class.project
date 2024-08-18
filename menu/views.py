from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def show_menu(request) :
    return render(request , 'menu/home.html')
    # return HttpResponse('به صفحه نمایش منو خوش آمدید')


def create_menu(request) :
    return render(request , 'menu/create.html')
    # return HttpResponse('به صفحه ایجاد منوی غذایی خوش آمدید')