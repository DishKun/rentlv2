from django.shortcuts import render,redirect

from workapp.models import Area,HouseInfo,UserInfo,Collect
from workapp.form import AppointForm,RegForm,LogForm,ModifyForm
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

import datetime

# Create your views here.


def index(request):
    area_list = Area.objects.all().order_by('?')[:3]
    # house_list = area_list[0].area_to.all().order_by('?')[:3]
    house_list = HouseInfo.objects.all().order_by('?')[:3]

    context={}

    # context['xuequ']=area_list[0].name
    context['area_list'] = area_list
    context['house_list'] = house_list
    if request.method == 'POST':
        area = request.POST['area']
        return redirect(to='list', id=area)
    return render(request, 'index.html', context)

def list(request,id):
    context={}

    counts = Area.objects.get(id=id).area_to.count()
    house_list = Area.objects.get(id=id).area_to.all()

    page_robot = Paginator(house_list,9)
    page_num = request.GET.get('page')
    try:
        house_list = page_robot.page(page_num)
    except EmptyPage:
        house_list = page_robot.page(page_robot.num_pages)
    except PageNotAnInteger:
        house_list = page_robot.page(1)

    context['area'] = Area.objects.get(id=id).name
    context['counts'] = counts
    context['house_list'] = house_list

    return render(request, 'list.html', context)

def detail(request,id):
    context={}
    house = HouseInfo.objects.get(id=id)
    area = house.area_to.all()[0].name
    context['house'] = house
    context['area'] = area
    installations = house.installations.split(" ")
    context['installations'] = installations
    return render(request, 'detail.html', context)

def userinfo(request):
    context={}
    user = request.user
    try:
        profile = UserInfo.objects.get(belong_to=user)
    except ObjectDoesNotExist:
        profile = UserInfo(belong_to=user,username=user.username,email=user.email)
        profile.save()
    try:
        collect_list = Collect.objects.filter(user=user)
        context['collect_list'] = collect_list
    except ObjectDoesNotExist:
        pass



    return render(request, 'personcenter.html', context)

def index_login(request):
    context={}
    if request.method == 'GET':
        form = LogForm
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email = email)

                if 'forget' in request.POST:
                    login(request,user)
                    return redirect(to="alteruser")

                if user.check_password(password):
                    login(request, user)
                    return redirect(to="index")
                else:
                    context['is_user'] = '你输入的邮箱或密码错误'

            except ObjectDoesNotExist:
                context['is_user'] = '你输入的邮箱或密码错误'







    context['form'] = form

    return render(request, 'login.html', context)

def register(request):
    context={}
    if request.method == 'GET':
        form = RegForm
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            c = User.objects.create_user(username=name, password=password,email=email)
            d = UserInfo(belong_to=c, username=name, email=email)
            c.save()
            d.save()
            return redirect(to="login")


    context['form'] = form

    return render(request, 'register.html', context)

def alteruser(request):
    if not isinstance(request.user, User):
        return redirect(to="login")

    user = request.user
    try:
        profile = UserInfo.objects.get(belong_to=user)
    except ObjectDoesNotExist:
        profile = UserInfo(belong_to=user,username=user.username,email=user.email)
        profile.save()

    context={}
    if request.method == 'GET':
        form = ModifyForm
    if request.method == 'POST':
        form = ModifyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            if name:
                profile.username = name
                profile.save()
            if password:
                user.set_password(password)
                user.save()
            return redirect(to='alteruser')



    context['form'] = form
    return render(request, 'personmodify.html', context)

def appointment(request, id):
    if not isinstance(request.user, User):
        return redirect(to="login")
    context = {}
    today = datetime.date.today()
    date_list = []
    for d in range(14):
        day = today + datetime.timedelta(days=d)
        t='%s年%s月%s日' %(day.year,day.month,day.day)
        date_list.append(t)
    time_list = ['08:00','09:00' ]
    for t in range(10,21):
        time_list.append(str(t)+':00')

    context['date_list'] = date_list
    context['time_list'] = time_list

    if request.method == 'GET':
        form = AppointForm


    if request.method == 'POST':
        form = AppointForm(request.POST)
        date = request.POST['date']
        time= request.POST['time']
        if form.is_valid():
            name= form.cleaned_data['name']
            phone= form.cleaned_data['phone']
            if date is '':
                date = '未选择日期'
            if time is '':
                time = '未选择时间'
            c = Collect(user=request.user,house_title_id=id,date=date,time=time,phone=phone)
            c.save()
            return redirect(to='userinfo')



    context['form'] = form


    return render(request, 'appointment.html', context)