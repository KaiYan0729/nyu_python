from django.http import HttpResponse
from django.template import loader
#from django.http import HttpResponse
from django.shortcuts import render
from .models import Category


def index(request):
    all_category = Category.objects.all()
    #context = {'all_category': all_category}
    return render(request, 'post/index.html', {'all_category': all_category})

def detail(request, category_id):
    return HttpResponse("<h2>Details for Post" + str(category_id) + "</h2>")
