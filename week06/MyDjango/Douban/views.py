from django.shortcuts import render

# Create your views here.
from .models import T1
from django.db.models import Avg

def books_short(request):
    ###  从models取数据传给template  ###
    shorts = T1.objects.filter( n_star__gt= 3)
    # 评论数量
    counter = T1.objects.all().count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg =f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "



    # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())

def search(request):

    keyw = request.GET.get('keyw', '')
    ###  从models取数据传给template  ###
    shorts = T1.objects.filter(short__icontains= keyw)
    # 评论数量
    counter = T1.objects.all().count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg =f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "


    return render(request, 'result.html', locals())
