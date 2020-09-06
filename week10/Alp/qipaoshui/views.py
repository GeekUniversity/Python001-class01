from django.shortcuts import render
from django.http import HttpResponse
from .models  import ProductInfo,Assessment
from .form import SearchForm
from django.utils import timezone
from datetime import  date

# Create your views here.

def get_index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            #读取表单的值
            cd = form.cleaned_data
            search_date = cd['date']
            curr_year = search_date.strftime("%Y")
            curr_month = search_date.strftime("%m")
            curr_day = search_date.strftime("%d")
            product_info = ProductInfo.objects.filter(spider_time__year=curr_year, spider_time__month=curr_month,
                                                      spider_time__day=curr_day). \
                extra(select={"spider_time": "DATE_FORMAT(spider_time, '%%Y-%%m-%%d ')"})
            return render(request, 'index.html', locals())

    # GET模式返回登录页面
    if request.method == 'GET':
        form = SearchForm()

        curr_year = timezone.now().strftime("%Y")
        curr_month = timezone.now().strftime("%m")
        curr_day = timezone.now().strftime("%d")
        today = date.today()
        product_info = ProductInfo.objects.filter(spider_time__year = curr_year ,spider_time__month = curr_month , spider_time__day = curr_day ).\
                          extra(select={"spider_time": "DATE_FORMAT(spider_time, '%%Y-%%m-%%d ')"})

        return render(request,'index.html',locals())

def get_charts(request):
    return render(request, 'charts.html')

def get_tables(request):
    return render(request, 'tables.html')


def get_detail(request):
    prod_id = request.GET.get('prod_id')

    product_info = ProductInfo.objects.filter(product_id = prod_id)
    comments_info = Assessment.objects.filter(product_id = prod_id)
    count = comments_info.count()
    print(product_info[0].product_name)
    return render(request, 'content.html',locals())

