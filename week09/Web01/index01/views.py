from django.shortcuts import render

# Create your views here.
from .form import LoginForm
from django.contrib.auth import  authenticate, login
from django.http import  HttpResponse
from django.http import  HttpResponseRedirect
def login2(request):
    # POST模式进行页面验证
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #读取表单的值
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request,user=user)
                # request.session['is_login'] = True
                # request.session['user_id'] = str(user.id)
                # request.session['user_name'] = str(user)
                return HttpResponseRedirect('index')
            else:
                return HttpResponseRedirect('error')
    # GET模式返回登录页面
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login2.html',locals())

def get_index(request):
    return  render(request,'index.html')


def get_error(request):
    return  render(request,'error.html')
